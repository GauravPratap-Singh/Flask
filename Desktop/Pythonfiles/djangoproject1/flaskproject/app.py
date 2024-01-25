from flask import Flask
import uuid
from flask_smorest import Api
import json
from resources.shop import blueprint as Shopblueprint
from resources.product import blueprint as Productblueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Shops REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"



api = Api(app)
api.register_blueprint(Shopblueprint)
api.register_blueprint(Productblueprint)



# GET - if we want some list/item from the server
# Post - if we want to create a new item/entry
# Put - if we want to update the entry
# delete - if we want to remove an entry    