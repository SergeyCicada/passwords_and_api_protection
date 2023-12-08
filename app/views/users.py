from flask import request
from flask_restx import Namespace, Resource
from marshmallow import Schema, fields

from app.container import user_service
from app.helpers.decorators import admin_required

user_ns = Namespace("users")

class UserSchema(Schema)
    id = fields.Int()
    username = fields.String()
    password = fields.String()
    role = fields.String()

@user_ns.route('/')
class UserView(Resource):
    def get(self):
        users = user_service.get_all()
        response = UserSchema(many=True).dump(users)

        return response, 200

    def post(self):
        data = request.json
        user = user_service.create(data)

        return "", 201, {"location": f"/users/{user.id}"}

@user_ns.route("/<int:id>")
class UserView(Resource):
    @admin_required
    def delete(self, uid):
        user_service.delete(uid)

        return "", 204