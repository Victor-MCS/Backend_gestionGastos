from flask import Blueprint

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET'])
def login():
    return "Login route"
