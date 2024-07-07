from flask_openapi3 import Tag
from flask_openapi3 import APIBlueprint
from flask import redirect

home_tag = Tag(name="Documentation",
               description="Documentation framework: Swagger, Redoc or RapiDoc")
home_api = APIBlueprint('/', __name__, url_prefix='', abp_tags=[home_tag])

@home_api.get('/', tags=[home_tag])
def home():
    """Redirect to /openapi, screen that lets you choose type of documentation.
    """
    return redirect('/openapi')