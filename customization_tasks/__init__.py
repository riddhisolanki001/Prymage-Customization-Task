version = "0.0.1"

from erpnext.controllers.selling_controller import SellingController
import frappe
from frappe import _, bold, throw
from frappe.utils import cint, flt, get_link_to_form, nowtime

from erpnext.accounts.party import render_address
from erpnext.controllers.accounts_controller import get_taxes_and_charges
from erpnext.controllers.sales_and_purchase_return import get_rate_for_return
from erpnext.controllers.stock_controller import StockController
from erpnext.stock.doctype.item.item import set_item_default
from erpnext.stock.get_item_details import get_bin_details, get_conversion_factor
from erpnext.stock.utils import get_incoming_rate, get_valuation_method

def new_update_stock_ledger(self):
    doctype = self.doctype 
    
        
    self.update_reserved_qty()
    sl_entries = []
    for d in self.items:
        if doctype == "Sales Invoice":
            quanity = d.custom_actual_qtyy
        else:
            quanity = d.qty
        if frappe.get_cached_value("Item", d.item_code, "is_stock_item") == 1 and flt(quanity):
            if flt(d.conversion_factor) == 0.0:
                d.conversion_factor = (
                    get_conversion_factor(d.item_code, d.uom).get("conversion_factor") or 1.0
                )

            if d.warehouse and (
                (not cint(self.is_return) and self.docstatus == 1)
                or (cint(self.is_return) and self.docstatus == 2)
            ):
                sl_entries.append(self.get_sle_for_source_warehouse(d))

            if d.target_warehouse:
                sl_entries.append(self.get_sle_for_target_warehouse(d))

            if d.warehouse and (
                (not cint(self.is_return) and self.docstatus == 2)
                or (cint(self.is_return) and self.docstatus == 1)
            ):
                sl_entries.append(self.get_sle_for_source_warehouse(d))

    self.make_sl_entries(sl_entries)
    
def new_get_sle_for_source_warehouse(self, item_row):
    doctype = self.doctype
    if doctype == "Sales Invoice":
        quantity = item_row.custom_actual_qtyy
    else:
        quantity = item_row.qty
    
    serial_and_batch_bundle = item_row.serial_and_batch_bundle
    if serial_and_batch_bundle and self.is_internal_transfer() and self.is_return:
        if self.docstatus == 1:
            serial_and_batch_bundle = self.make_package_for_transfer(
                serial_and_batch_bundle, item_row.warehouse, type_of_transaction="Inward"
            )
        else:
            serial_and_batch_bundle = frappe.db.get_value(
                "Stock Ledger Entry",
                {"voucher_detail_no": item_row.name, "warehouse": item_row.warehouse},
                "serial_and_batch_bundle",
            )

    sle = self.get_sl_entries(
        item_row,
        {
            "actual_qty": -1 * flt(quantity),
            "incoming_rate": item_row.incoming_rate,
            "recalculate_rate": cint(self.is_return),
            "serial_and_batch_bundle": serial_and_batch_bundle,
        },
    )
    if item_row.target_warehouse and not cint(self.is_return):
        sle.dependant_sle_voucher_detail_no = item_row.name

    return sle


def new_get_sle_for_target_warehouse(self, item_row):
    doctype = self.doctype
    if doctype == "Sales Invoice":
        quantity = item_row.custom_actual_qtyy
    else:
        quantity = item_row.qty
    
    sle = self.get_sl_entries(
        item_row, {"actual_qty": flt(quantity), "warehouse": item_row.target_warehouse}
    )

    if self.docstatus == 1:
        if not cint(self.is_return):
            sle.update({"incoming_rate": item_row.incoming_rate, "recalculate_rate": 1})
        else:
            sle.update({"outgoing_rate": item_row.incoming_rate})
            if item_row.warehouse:
                sle.dependant_sle_voucher_detail_no = item_row.name

    if item_row.serial_and_batch_bundle and not cint(self.is_return):
        type_of_transaction = "Inward"
        if cint(self.is_return):
            type_of_transaction = "Outward"

        sle["serial_and_batch_bundle"] = self.make_package_for_transfer(
            item_row.serial_and_batch_bundle,
            item_row.target_warehouse,
            type_of_transaction=type_of_transaction,
        )

    return sle


SellingController.update_stock_ledger = new_update_stock_ledger
SellingController.get_sle_for_source_warehouse = new_get_sle_for_source_warehouse
SellingController.get_sle_for_target_warehouse = new_get_sle_for_target_warehouse