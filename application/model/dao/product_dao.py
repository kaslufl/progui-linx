import json
from application.model.entity.product import Product

class Product_DAO:
    def __init__(self):
        self.json_list = []
        self.product_list = []

    def get_products_json(self):
        with open('C:\Users\Lucas Leal\Desktop\progui-linx\products.json') as product_file
        self.json_list = json.load(product_file)
        for product in self.json_list:
            self.product_list.append(Product(product['id'], product['name'], product['image'], product['oldPrice'], product['price'], product['description'], product['installments']['count'], product['installments']['value']))

    def get_product_list(self):
        return self.product_list