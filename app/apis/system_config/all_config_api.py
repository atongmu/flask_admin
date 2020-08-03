# -*- coding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with
from app.apis.api_constant import HTTP_OK
from app.models import ConfigDefault

config_fields = {
    "id": fields.Integer,
    "title": fields.String,
    "name": fields.String,
    "value": fields.String,
}
single_config_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(config_fields))
}


class ConfigAllResource(Resource):
    """站点配置列表"""

    @marshal_with(single_config_fields)
    def get(self):
        config_default = ConfigDefault().query.all()
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功",
            "data": config_default
        }
        return data
