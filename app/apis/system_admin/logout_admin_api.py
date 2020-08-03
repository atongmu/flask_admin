# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse
from app.apis.api_constant import HTTP_OK

parse_base = reqparse.RequestParser()
parse_base.add_argument("Authorization", location='headers', help=u"请输入请求参数")


class AdminLogoutResource(Resource):
    """管理员退出"""

    def get(self):

        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
