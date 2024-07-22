app_name = "erp"
app_title = "ERP"
app_publisher = "Sanskar Technolab"
app_description = "ERP"
app_email = "meet@sanskartechnolab.com"
app_license = "mit"
required_apps = ["frappe/erpnext"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erp/css/erp.css"
# app_include_js = "/assets/erp/js/erp.js"

# include js, css files in header of web template
# web_include_css = "/assets/erp/css/erp.css"
# web_include_js = "/assets/erp/js/erp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "erp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {
#     "Sales Invoice" : "public/js/sales_invoice.js",
# }
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "erp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "erp.utils.jinja_methods",
# 	"filters": "erp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "erp.install.before_install"
# after_install = "erp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "erp.uninstall.before_uninstall"
# after_uninstall = "erp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "erp.utils.before_app_install"
# after_app_install = "erp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "erp.utils.before_app_uninstall"
# after_app_uninstall = "erp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	# "Sales Invoice": "erp.public.py.sales_invoice.SellingController",
	# "erpnext.controllers.SellingController.StockController": "erp.public.py.sales_invoice.SellingController",
	# "erpnext.accounts.doctype.sales_invoice.SalesInvoice.SellingController": "erp.public.py.sales_invoice.SellingController"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"erp.tasks.all"
# 	],
# 	"daily": [
# 		"erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"erp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"erp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "erp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erp.event.get_events"
# }
# override_whitelisted_methods = {
#     "erpnext.controllers.selling_controller.SellingController.update_stock_ledger": "erp.public.py.sales_invoice.new_update_stock_ledger",
#     "erpnext.controllers.selling_controller.SellingController.get_sle_for_source_warehouse": "erp.public.py.sales_invoice.new_get_sle_for_source_warehouse",
#     "erpnext.controllers.selling_controller.SellingController.get_sle_for_target_warehouse": "erp.public.py.sales_invoice.new_get_sle_for_target_warehouse",
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "erp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["erp.utils.before_request"]
# after_request = ["erp.utils.after_request"]

# Job Events
# ----------
# before_job = ["erp.utils.before_job"]
# after_job = ["erp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"erp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


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