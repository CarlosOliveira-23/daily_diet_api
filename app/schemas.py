from marshmallow import Schema, fields


class MealSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    calories = fields.Float(required=True)
    user_id = fields.Int(required=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    meals = fields.Nested(MealSchema, many=True)