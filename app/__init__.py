from flask import Flask
from flask_cors import CORS
from app.config import Config
from app.utils.db import init_db
from app.auth.controller.auth_controller import auth_bp
from app.usuarios.controllers.usuario_controller import usuario_bp
from app.tarjetas.controllers.tarjetas_controller import tarjetas_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
    app.register_blueprint(tarjetas_bp, url_prefix='/api/tarjetas')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    return app
