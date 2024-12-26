from flask import Flask
from configs.config import apply_config_to_app
from routes.rating_route import api


def create_app():
    flask_app = Flask(__name__)

    # Apply configuration
    apply_config_to_app(flask_app)

    # Register blueprints or extensions
    flask_app.register_blueprint(api)

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
