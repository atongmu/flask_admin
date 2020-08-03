# -*- coding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with, reqparse
from app.apis.api_constant import HTTP_OK
from app.models import Managers

parse_base = reqparse.RequestParser()
parse_base.add_argument('page_no', type=int, required=True, help=u"请输入请求参数")
parse_base.add_argument('page_size', type=int, required=True, help=u"请输入请求参数")

admin_fields = {
    "id": fields.Integer,
    "avatar": fields.String,
    "users_name": fields.String,
    "is_administrator": fields.Boolean,
}
admin_page = {
    "has_next": fields.Boolean,
    "has_prev": fields.Boolean,
    "next_num": fields.Integer,
    "prev_num": fields.Integer,
    "pages": fields.Integer,
    "items": fields.List(fields.Nested(admin_fields)),
    "total": fields.Integer
}
single_admin_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(admin_fields)
}


class AdminPageResource(Resource):
    """用户列表"""

    @marshal_with(single_admin_fields)
    def get(self):
        args = parse_base.parse_args()
        page_no = args.get("page_no")
        page_size = args.get("page_size")
        admin_default = Managers.query.order_by(Managers.id.desc()).paginate(page_no, page_size)
        data = {
            "status": HTTP_OK,
            "msg": u"获取成功",
            "data": admin_default
        }
        return data
