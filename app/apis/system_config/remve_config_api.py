# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import ConfigDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("c_id", type=int, required=True, help=u"请输入请求参数")


class ConfigRemoveResource(Resource):
    """站点配置删除"""

    def post(self):
        args = parse_base.parse_args()
        c_id = args.get("c_id")
        config_default = ConfigDefault.query.get(c_id)
        if not config_default.is_delete():
            abort(404, msg=u"操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
