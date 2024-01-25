from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import Flask, jsonify, request
import uuid
from db import products


blueprint = Blueprint("products",__name__,description="Operation on products")


@blueprint.route("/product/<product_id>")
class Product(MethodView):
    def get(self,product_id):
        try:
            return products[product_id]
        except KeyError:
            abort(404, message="Product not found")
            

    def delete(self,product_id):
        try:
            del products[product_id]
            abort(404, message="Product delete")
        except KeyError:
            abort(404, message="Product not found")

    def put(self,product_id):
        product_data = request.json
        if "price" not in product_data or "name" not in product_data:
            abort(404, message="please ensure 'price' and 'name' are included in request")
        try:
            product = products[product_id]
            # | = merge the dictionaries
            product |= product_data
            return product
        except KeyError:
            abort(404, message="Product not found")


@blueprint.route("/product")
class ProductList(MethodView):
    def get(self):
        return {"products": list(products.values())}
    
    def post(self):
        new_product = request.json
        if ("price" not in new_product
            or "shop_id" not in new_product
            or "name" not in new_product):
            abort(404, message="please ensure 'price','shop_id' and 'name' are included in request")
        for product in products.values():
            if (new_product["name"]==product["name"]
                and new_product["shop_id"]==product["shop_id"]):
                abort(400,"Product already exists")   
        product_id = uuid.uuid4().hex
        product = {**new_product,"id": product_id}
        products[product_id] = product

        return product