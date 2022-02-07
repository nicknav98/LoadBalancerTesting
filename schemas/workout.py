from marshmallow import Schema, fields, post_dump, validate, validates, ValidationError

from schemas.user import UserSchema


class WorkoutSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=[validate.Length(max=100)])
    length = fields.String(validate=[validate.Length(max=100)])
    directions = fields.String(validate=[validate.Length(max=300)])
    body_part = fields.String(validate=[validate.Length(max=150)])
    is_publish = fields.Boolean(dump_only=True)

    author = fields.Nested(UserSchema, attribute='user', dump_only=True, only=['id', 'username'])

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @post_dump(pass_many=True)
    def wrap(self, data, many, **kwargs):
        if many:
            return {'data': data}
        return data
