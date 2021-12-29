from os import environ


APP_HOST = environ.get("APP_HOST", "0.0.0.0")
APP_PORT = int(environ.get("APP_PORT", 8003))
