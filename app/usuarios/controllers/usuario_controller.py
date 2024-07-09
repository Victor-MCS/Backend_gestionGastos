from flask import Blueprint, request, jsonify
from app.usuarios.services.usuario_services import UsuarioService
from app.usuarios.schemas import RegistroSchema

usuario_bp = Blueprint('usuario', __name__)

registro_schema = RegistroSchema()
registros_schema = RegistroSchema(many=True)

@usuario_bp.route('/', methods=['GET'])
def get_usuarios():
    registros = UsuarioService.get_all()
    return jsonify(registros), 200

@usuario_bp.route('/<int:id>', methods=['GET'])
def get_usuario(id):
    registro = UsuarioService.get_by_id(id)
    if not registro:
        return jsonify({'error': 'Registro no encontrado'}), 404
    return jsonify(registro), 200

@usuario_bp.route('/', methods=['POST'])
def create_ususario():
    data = request.get_json()
    errors = registro_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    registro = UsuarioService.create(data)
    if "error" in registro:
        return jsonify(registro), 400
    return jsonify(registro), 201


@usuario_bp.route('/<int:id>', methods=['PUT'])
def update_ususario(id):
    data = request.get_json()
    errors = registro_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    registro = UsuarioService.update(id, data)
    result = registro_schema.dump(registro) 
    return jsonify(result), 200

@usuario_bp.route('/<int:id>', methods=['DELETE'])
def delete_usuairo(id):
    UsuarioService.delete(id)
    return jsonify({'message': 'Registro eliminado'}), 200
