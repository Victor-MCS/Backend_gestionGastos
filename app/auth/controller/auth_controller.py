from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth.services.auth_services import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')

    if not email or not password:
        return jsonify({'error': 'Nombre de usuario y contraseña requeridos'}), 400

    # No se como deshashear de momento xd
    # hashed_password = generate_password_hash(password)
    AuthService.create_user(email, name, password)

    return jsonify({'message': 'Usuario creado correctamente'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'error': 'Nombre de usuario y contraseña requeridos'}), 400

    # hashed_password = generate_password_hash(password)
    # print(hashed_password)
    user = AuthService.get_user(email, password)

    if not user:
        return jsonify({'error': 'Credenciales incorrectas'}), 401

    return jsonify({'message': 'Inicio de sesión exitoso'}, user[0],user[1]), 200