from app.settings import APP_HOST, APP_PORT
from app import view as application


def main() -> None:
    application.app.run(debug=True, host=APP_HOST, port=APP_PORT)


if __name__ == "__main__":
    main()
