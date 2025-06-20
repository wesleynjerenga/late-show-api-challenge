"""
Flask application entry point for the Late Show API Challenge.
This app provides RESTful endpoints for managing episodes, guests, and appearances for a late show database.
"""
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .models import db
import os

# Import all models for migrations
from .models import User, Guest, Episode, Appearance

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config.Config')

    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    @app.errorhandler(Exception)
    def handle_exception(e):
        response = {
            "error": str(e),
            "type": e.__class__.__name__
        }
        return jsonify(response), 500

    # Register blueprints here (to be implemented)
    from .controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)
    from .controllers.guest_controller import guest_bp
    app.register_blueprint(guest_bp)
    from .controllers.episode_controller import episode_bp
    app.register_blueprint(episode_bp)
    from .controllers.appearance_controller import appearance_bp
    app.register_blueprint(appearance_bp)
    from .controllers.health_controller import health_bp
    app.register_blueprint(health_bp)
    # ...

    return app

app = create_app()
