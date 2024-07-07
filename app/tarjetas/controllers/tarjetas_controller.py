from flask import Blueprint, request, jsonify
from app.tarjetas.services.tarjetas_services import TarjetasService
from app.tarjetas.schemas import RegistroSchema

tarjetas_bp = Blueprint('tarjetas', __name__)

registro_schema = RegistroSchema()
registros_schema = RegistroSchema(many=True)

@tarjetas_bp.route('/', methods=['GET'])
def get_registros():
    registros = TarjetasService.get_all()
    return jsonify(registros), 200

@tarjetas_bp.route('/<int:id>', methods=['GET'])
def get_registro(id):
    registro = TarjetasService.get_by_id(id)
    if not registro:
        return jsonify({'error': 'Registro no encontrado'}), 404
    return jsonify(registro), 200

@tarjetas_bp.route('/', methods=['POST'])
def create_registro():
    data = request.get_json()
    errors = registro_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    registro = TarjetasService.create(data)
    result = registro_schema.dump(registro) 
    return jsonify(result), 201

@tarjetas_bp.route('/<int:id>', methods=['PUT'])
def update_registro(id):
    data = request.get_json()
    errors = registro_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    registro = TarjetasService.update(id, data)
    result = registro_schema.dump(registro) 
    return jsonify(result), 200

@tarjetas_bp.route('/<int:id>', methods=['DELETE'])
def delete_registro(id):
    TarjetasService.delete(id)
    return jsonify({'message': 'Registro eliminado'}), 200
