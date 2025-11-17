from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Table 1: Products Data
products_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Products.csv")

# Table 2: Customer Data
customer_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Customers.csv")


# Table 3: Categories
categories_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Categories.csv")

# Table 4 : Employees
employees_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Employees.csv")

# Table 5 : Order_Details
order_details_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Order_Details.csv")

# Table 6 :Suppliers
suppliers_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Suppliers.csv")

# Table 7 : Shippers
shippers_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Shippers.csv")

# Table 8 : Orders
orders_data = pd.read_csv("C:\\Contents\\Cigna\\Excel\\Orders.csv")


@app.route('/tables', methods=['GET'])
def get_tables():
    result = {
        "products_data": products_data.to_dict(orient="records"),
        "customers_data": customer_data.to_dict(orient="records"),
        "categories_data": categories_data.to_dict(orient="records"),
        "employees_data": employees_data.to_dict(orient="records"),
        "order_details_data": order_details_data.to_dict(orient="records"),
        "suppliers_data": suppliers_data.to_dict(orient="records"),
        "shippers_data": shippers_data.to_dict(orient="records"),
        "orders_data": orders_data.to_dict(orient="records")
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
