# -*- coding: utf-8 -*-
from flask import g
from flask_restful import Resource, fields, marshal_with
from app.apis.api_constant import HTTP_OK

admin_fields = {
    "id": fields.Integer,
    "avatar": fields.String,
    "users_name": fields.String,
    "is_administrator": fields.Boolean,
}
single_admin_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(admin_fields)
}


class AdminInfoResource(Resource):
    """用户详情"""
    @marshal_with(single_admin_fields)
    def get(self):
        current_user = g.manager
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": current_user
        }
        return data
