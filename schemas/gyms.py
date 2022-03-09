from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError


class GymSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    gymName = fields.String(required=True, validate=[validate.Length(max=50)])
    pricePerMonth = fields.Integer(dump_only=True)
    is_open = fields.Boolean(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data
