import os

from flask_openapi3 import Info

from database.database import Database
from log.log import Log
from resources.settings import Settings

API_TITLE = os.environ.get("API_TITLE")
VERSION = os.environ.get("VERSION")
SECRET_KEY = os.environ.get("SECRET_KEY")
PORT = int(os.environ.get("PORT"))
HOST = os.environ.get("HOST")

INFORMATION = Info(title=API_TITLE, version=VERSION)

flask_settings = Settings(
    information=INFORMATION, secret_key=SECRET_KEY, port=PORT, host=HOST
)
flask_settings.generate_app()

app = flask_settings.app
database = Database()
log = Log()
