from flask import Blueprint, Flask
from flask_restx import Api

import app.resources as resources
from app.config.database import init_db


def create_app(**kwargs):
    flask_app = Flask(__name__)
    blueprint = Blueprint("api", __name__)

    flask_app.config["RESTX_MASK_SWAGGER"] = False
    flask_app.config.from_object("app.config.config.Config")

    init_db(flask_app)

    api = Api(
        app=blueprint,
        doc="/",
        description="Flask-resxの練習",
        title="flask-restx-training-api",
    )
    flask_app.register_blueprint(blueprint, url_prefix="/api")
    resources.setup(api)

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run()
