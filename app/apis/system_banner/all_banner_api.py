# -*- coding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with
from app.apis.api_constant import HTTP_OK
from app.models import BannerDefault

banner_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "url": fields.String,
    "desc": fields.String,
}
single_banner_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(banner_fields))
}


class BannerALLResource(Resource):
    """轮播列表"""

    @marshal_with(single_banner_fields)
    def get(self):
        banner_default = BannerDefault.query.all()
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功",
            "data": banner_default
        }
        return data
