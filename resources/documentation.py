from flask import redirect
from flask_openapi3 import Tag

from app import app, log

TAG_DOCUMENTATION = Tag(
    name="Documentation",
    description="Documentation selection: Swagger, Redoc or RapiDoc.",
)


@app.get("/", tags=[TAG_DOCUMENTATION])
def documentation_route():
    """
    Redirects to the /openapi route,\
    a screen that allows choosing the documentation style.
    """
    log.add_message("Documentation accessed")
    log.add_message("")

    return redirect("/openapi")
