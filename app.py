from flask_openapi3 import OpenAPI, Info, Tag

from models import Session, Group
from routes import home_api, expenses_api, groups_api, stats_api
from flask_cors import CORS

info = Info(title="Personal Finance Manager", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)
app.register_api(home_api)
app.register_api(expenses_api)
app.register_api(groups_api)
app.register_api(stats_api)
