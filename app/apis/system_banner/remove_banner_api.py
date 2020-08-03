# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import BannerDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("b_id", type=int, required=True, help=u"请输入请求参数")


class BannerRemoveResource(Resource):
    """轮播删除"""

    def post(self):
        args = parse_base.parse_args()
        b_id = args.get("b_id")
        banner_default = BannerDefault.query.get(b_id)
        if not banner_default.is_delete():
            abort(404, msg=u"操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
