import marshmallow
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from project.configs import Config


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()


def register_blueprints(app):
    from project.endpoints.deliveries import blueprint as pedidos
    from project.endpoints.status import blueprint as status

    app.register_blueprint(pedidos)
    app.register_blueprint(status)


def register_error_handler(app):
    @app.errorhandler(marshmallow.exceptions.ValidationError)
    def validation_error_handler(e):
        return jsonify(e.messages), 400


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)
    register_error_handler(app)

    return app
