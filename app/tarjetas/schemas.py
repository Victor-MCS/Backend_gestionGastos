from marshmallow import Schema, fields

class TarjetasSchema(Schema):
    idTarjeta = fields.Int(dump_only=True)
    amount = fields.Int(required=True)
    name = fields.Str(required=True)
    idTipo = fields.Int(required=False)
    idUser = fields.Int(required=False)
    listIdIngresos = fields.List(fields.Integer(), required=False)
    listIdGastos = fields.List(fields.Integer(), required=False)