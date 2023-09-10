from flask_cors import CORS
from flask_openapi3 import Info, OpenAPI


class Settings:
    """Class to define all Flask settings"""

    def __init__(
        self, information: Info, secret_key: str, port: int, host: str
    ):
        self._app = None
        self._information = information
        self._secret_key = secret_key
        self._port = port
        self._host = host

    @property
    def app(self):
        """Method to return app"""
        return self._app

    def generate_app(self) -> None:
        """Method to generate app"""
        self._app = OpenAPI(__name__, info=self._information)
        self._app.secret_key = self._secret_key
        CORS(self._app)

    def run_aplication(self) -> None:
        """Method to start the flask aplication"""
        if self._app is None:
            self.generate_app()

        self._app.run(debug=True, port=self._port, host=self._host)
