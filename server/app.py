from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from .models import db
import os

# Import all models for migrations
from .models import User, Guest, Episode, Appearance

def create_app():
    app = Flask(__name__)
    app.config.from_object('server.config')

    db.init_app(app)
    jwt = JWTManager(app)
    migrate = Migrate(app, db)

    # Register blueprints here (to be implemented)
    from .controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)
    from .controllers.guest_controller import guest_bp
    app.register_blueprint(guest_bp)
    from .controllers.episode_controller import episode_bp
    app.register_blueprint(episode_bp)
    from .controllers.appearance_controller import appearance_bp
    app.register_blueprint(appearance_bp)
    # ...

    return app

app = create_app()
