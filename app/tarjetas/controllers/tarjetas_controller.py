from flask import Blueprint, request, jsonify
from app.tarjetas.services.tarjetas_services import TarjetasService
from app.tarjetas.schemas import TarjetasSchema

tarjetas_bp = Blueprint('tarjetas', __name__)

tarjeta_schema = TarjetasSchema()
tarjetas_schema = TarjetasSchema(many=True)

@tarjetas_bp.route('/<int:id>', methods=['GET'])
def get_tarjetas(id):
    registros = TarjetasService.get_all(id)
    return jsonify(registros), 200

@tarjetas_bp.route('/profile/<int:id>', methods=['GET'])
def get_tarjeta(id):
    registro = TarjetasService.get_by_id(id)
    if not registro:
        return jsonify({'error': 'Registro no encontrado'}), 404
    return jsonify(registro), 200

@tarjetas_bp.route('/', methods=['POST'])
def create_tarjeta():
    data = request.get_json()
    errors = tarjeta_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    registro = TarjetasService.create(data)
    result = tarjeta_schema.dump(registro) 
    return result, 201

@tarjetas_bp.route('/<int:id>', methods=['PUT'])
def update_registro(id):
    data = request.get_json()
    errors = tarjeta_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    registro = TarjetasService.update(id, data)
    result = tarjeta_schema.dump(registro) 
    return jsonify(result), 200

@tarjetas_bp.route('/<int:id>', methods=['DELETE'])
def delete_registro(id):
    TarjetasService.delete(id)
    return jsonify({'message': 'Registro eliminado'}), 200
