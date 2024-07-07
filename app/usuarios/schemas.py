from marshmallow import Schema, fields

class RegistroSchema(Schema):
    id = fields.Int(dump_only=True)
    campo1 = fields.Str(required=True)
    campo2 = fields.Str(required=True)
    # Agrega aquí los demás campos
