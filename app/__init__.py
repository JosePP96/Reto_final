from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_dict, TestConfig

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    if config_name == "test":
        app.config.from_object(TestConfig)
    else:
        app.config.from_object(config_dict[config_name])

    # Initialize the database
    db.init_app(app)

    # Import blueprints/routes
    from app.routes import data_routes

    # Register blueprints
    app.register_blueprint(data_routes)

    return app
