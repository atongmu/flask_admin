# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import ConfigDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("title", type=str, required=True, help=u"请输入请求参数")
parse_base.add_argument("name", type=str, required=True, help=u"请输入请求参数")
parse_base.add_argument("value", type=str, required=True, help=u"请输入请求参数")


class ConfigAppendResource(Resource):
    """站点配置注册"""

    def post(self):
        args = parse_base.parse_args()
        title = args.get("title")
        name = args.get("name")
        value = args.get("value")
        config_default = ConfigDefault()
        config_default.title = title
        config_default.name = name
        config_default.value = value
        if not config_default.is_save():
            abort(404, msg=u"站点配置注册失败")
        data = {
            "status": HTTP_OK,
            "msg": u"注册成功"
        }
        return data
