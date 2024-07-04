from flask import Blueprint

# Create a main blueprint to register all blueprints
bp = Blueprint('api', __name__)

from app.routes.auth import bp as auth_bp
from app.routes.expenses import bp as expenses_bp
from app.routes.users import bp as users_bp

# Register blueprints
bp.register_blueprint(auth_bp)
bp.register_blueprint(expenses_bp)
bp.register_blueprint(users_bp)
