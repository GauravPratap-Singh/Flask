from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import Flask, jsonify, request
import uuid
from db import shops


blueprint = Blueprint("shops",__name__,description="Operation on shops")

@blueprint.route("/shop/<shop_id>")
class Shop(MethodView):
    def get(self, shop_id):
        try:
            return shops[shop_id]
        except KeyError:
            abort(404, message="Shop not found")
            


    def delete(self, shop_id):
        try:
            del shops[shop_id]
            abort(404, message="Shop deleted")
        except KeyError:
            abort(404, message="Shop not found")
            

@blueprint.route("/shop")
class ShopList(MethodView):
    def get(self):
        return {"shops": list(shops.values())}

    def post(self):
        shop_data = request.json
        if "name" not in shop_data:
            abort(400,message="please make sure 'name' is included in request")

        for shop in shops.values():
            if shop_data["name"] == shop["name"]:
                abort(400,message="shop already existed")      
        shop_id = uuid.uuid4().hex
        shop = {**shop_data,"id":shop_id}
        shops[shop_id] = shop
        return shop          