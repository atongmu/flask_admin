# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import PostersDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("p_id", type=int, required=True, help=u"请输入请求参数")
parse_base.add_argument("name", type=str, required=True, help=u"请输入请求参数")
parse_base.add_argument("url", type=str, required=True, help=u"请输入请求参数")
parse_base.add_argument("desc", type=str, help=u"请输入请求参数")


class PosterUpdateResource(Resource):
    """广告注册"""

    def post(self):
        args = parse_base.parse_args()
        p_id = args.get("p_id")
        name = args.get("name")
        url = args.get("url")
        desc = args.get("desc")
        poster_default = PostersDefault.query.get(p_id)
        poster_default.name = name
        poster_default.url = url
        if desc:
            poster_default.desc = desc
        if not poster_default.is_update():
            abort(404, msg=u"操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
