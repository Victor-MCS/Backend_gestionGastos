from marshmallow import Schema, fields

class RegistroSchema(Schema):
    email = fields.Str(required=True)
    name = fields.Str(required=True)
    password= fields.Str(required=True)
