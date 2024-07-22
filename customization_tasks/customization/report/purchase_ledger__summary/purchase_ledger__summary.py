import frappe

def execute(filters=None):
    columns, data = [], []

    columns = [
        {
            "label": "Purchase Type Name",
            "fieldname": "purchase_type_name",
            "fieldtype": "Data",
            "width": 350,
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 150,
        },
        
        {
            "label": "Grand Total",
            "fieldname": "total",
            "fieldtype": "Currency",
            "width": 150,
        },
    ]

    sql = """
        SELECT
            custom_purchase_type AS purchase_type_name,
            SUM(total) AS amount,
            SUM(grand_total) as total
        FROM
            `tabPurchase Invoice`
        WHERE
            docstatus = 1
    """

    conditions = []
    sql_args = []
# test comment for git
	# This is the test comment
 #test comment
    if filters:
        if filters.get("start_date"):
            conditions.append("posting_date >= %s")
            sql_args.append(filters.get("start_date"))

        if filters.get("end_date"):
            conditions.append("posting_date<= %s")
            sql_args.append(filters.get("end_date"))
        
        if filters.get("purchase_type"):
            conditions.append("custom_purchase_type= %s")
            sql_args.append(filters.get("purchase_type"))   
            
        if filters.get("suppliers"):
            conditions.append("supplier= %s")
            sql_args.append(filters.get("suppliers"))      

    if conditions:
        sql += " AND " + " AND ".join(conditions)

    sql += """
			GROUP BY custom_purchase_type
    """

    data = frappe.db.sql(sql, tuple(sql_args), as_dict=True)

    return columns, data
