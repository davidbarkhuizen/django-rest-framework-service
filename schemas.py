from marshmallow import Schema, fields

class Currency(Schema):
    symbol = fields.Str(required=True)
    decimal_places = fields.Int(required=True)

class Country(Schema):
    name = fields.Str(required=True)
    alpha2 = fields.Str(required=True)
    alpha3 = fields.Str(required=True)
    currencies = fields.List(fields.Nested(Currency()))