// Copyright (c) 2024, riddhi and contributors
// For license information, please see license.txt

frappe.query_reports["Purchase Ledger Summary"] = {
	"filters": [

        {
            "label": "Supplier",
            "fieldname": "suppliers",
            "fieldtype": "Link",
			"options":"Supplier"
        },
		
		{
			"fieldname": "purchase_type",
			"fieldtype": "Select",
			"label": "Purchase Type",
			"options": "\nRaw Material Purchase - Scrap\nRaw Material Purchase- Billets\nImport Purchase- Spares\nImport Purchase- Consumables\nLocal Purchase- Spares & Consumables\nTrade Purchase - Others\nTrade Purchase- Iron Rods\nTrade Purchase - Profiles\nMiscellaneous Purchase\nGeneral Purchase"
		},

        {
            "label": "Start Date",
            "fieldname": "start_date",
            "fieldtype": "Date"
        },
        {
            "label": "End Date",
            "fieldname": "end_date",
            "fieldtype": "Date"
        },

		
		

	]
};
