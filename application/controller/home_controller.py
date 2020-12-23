from application import app
from flask import render_template, request
from application.model.dao.product_dao import Product_DAO

@app.route("/")
@app.route("/home")
def home():
    product_dao = Product_DAO
    product_dao.get_products_json()
    product_list = product_dao.get_product_list()
    return render_template("home.html", product_list = product_list)