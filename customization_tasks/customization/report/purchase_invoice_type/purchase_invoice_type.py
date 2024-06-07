# Copyright (c) 2024, Sanskar Technolab Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe import _


def execute(filters=None):
	columns = [
		{"label": _("<b>Purchase Invoice ID</b>"), "fieldname": "name", "fieldtype": "Link", "options": "Purchase Invoice", "width":150},
		{"label": _("<b>Date</b>"), "fieldname": "posting_date", "fieldtype": "Date", "width":100},
		{"label": _("<b>Company</b>"), "fieldname": "company", "fieldtype": "Link", "options": "Company", "width":150},
		{"label": _("<b>Supplier</b>"), "fieldname": "supplier", "fieldtype": "Data", "width":150},
		{"label": _("<b>Purchase Type</b>"), "fieldname": "custom_purchase_type", "fieldtype": "Data", "width":150},
		{"label": _("<b>Currency</b>"), "fieldname": "currency", "fieldtype": "Data", "width":100},
		{"label": _("<b>Exchange Rate</b>"), "fieldname": "conversion_rate", "fieldtype": "Data", "width":100},
		{"label": _("<b>Item Code</b>"), "fieldname": "item_code", "fieldtype": "Data", "width":100},
		{"label": _("<b>Quantity</b>"), "fieldname": "qty", "fieldtype": "Float", "width":100},
		{"label": _("<b>Rate</b>"), "fieldname": "rate", "fieldtype": "Currency", "width":100},
		{"label": _("<b>Amount</b>"), "fieldname": "amount", "fieldtype": "Currency", "width":100},
		{"label": _("<b>Due Date</b>"), "fieldname": "due_date", "fieldtype": "Data", "width":100},
		{"label": _("<b>Grand Total</b>"), "fieldname": "grand_total", "fieldtype": "Currency", "width":100},
	]

	sql = f"""
			SELECT
				P.name,
                P.currency,
                P.conversion_rate,
                P.due_date,
                P.grand_total,
				DATE(P.creation) as posting_date,
				P.company,
				P.supplier,
				P.custom_purchase_type,
				PI.item_code,
				PI.qty,
				PI.rate,
				PI.amount
			FROM `tabPurchase Invoice` AS P
			JOIN `tabPurchase Invoice Item` AS PI ON P.name = PI.parent
			WHERE P.docstatus = 1
			"""

	if filters.get('from_date') and filters.get('to_date'):
		sql += f"AND DATE(P.creation) BETWEEN '{filters.get('from_date')}' AND '{filters.get('to_date')}'"
	if filters.get('supplier'):
		sql += f"AND P.supplier  = '{filters.get('supplier')}'"
	sql += f"ORDER BY P.name"

	data = frappe.db.sql(sql,as_dict = True)
	return columns, data