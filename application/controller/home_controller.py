from application import app
from flask import render_template, request
from application.model.entity.product import Product

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")