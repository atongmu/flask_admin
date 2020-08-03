# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import BannerDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("name", type=str, required=True, help=u"请输入请求参数")
parse_base.add_argument("url", type=str, required=True, help=u"请输入请求参数")
parse_base.add_argument("desc", type=str, help=u"请输入请求参数")


class BannerAppendResource(Resource):
    """轮播注册"""

    def post(self):
        args = parse_base.parse_args()
        name = args.get("name")
        url = args.get("url")
        desc = args.get("desc")
        banner_default = BannerDefault()
        banner_default.name = name
        banner_default.url = url
        if desc:
            banner_default.desc = desc
        if not banner_default.is_save():
            abort(404, msg=u"轮播注册失败")
        data = {
            "status": HTTP_OK,
            "msg": u"注册成功"
        }
        return data
