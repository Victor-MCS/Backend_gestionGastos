from flask import Flask
from app.routes import bp as main_bp
from app.utils.database import init_db

def create_app():
    app = Flask(__name__)

    # Initialize database connection
    init_db()

    # Register main blueprint
    app.register_blueprint(main_bp)

    return app
