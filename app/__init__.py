from flask import Flask
from app.config import Config
from app.utils.db import init_db
from app.usuarios.controllers.usuario_controller import usuario_bp
from app.tarjetas.controllers.tarjetas_controller import tarjetas_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    # registro usuarios
    app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
    # registro tarjetas
    app.register_blueprint(tarjetas_bp,url_prefix='/api/tarjetas')

    return app
