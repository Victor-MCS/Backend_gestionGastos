from flask import Blueprint

bp = Blueprint('users', __name__, url_prefix='/users')

@bp.route('/profile', methods=['GET'])
def profile():
    return "User profile route"
