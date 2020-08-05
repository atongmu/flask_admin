# -*- coding: utf-8 -*-
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource, fields, marshal_with
from app.apis.api_constant import HTTP_OK
from app.apis.system_admin.admin_utils import get_admin

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
    @jwt_required
    def get(self):
        u_id = get_jwt_identity()
        current_user = get_admin(u_id)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": current_user
        }
        return data
