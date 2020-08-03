# -*- coding: utf-8 -*-
from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.models import ImageDefault

parse_base = reqparse.RequestParser()
parse_base.add_argument("i_id", type=int, required=True, help=u"请输入请求参数")


class ImageRemoveResource(Resource):
    """图片删除"""

    def post(self):
        args = parse_base.parse_args()
        i_id = args.get("i_id")
        image_default = ImageDefault.query.get(i_id)
        if not image_default.delete_file:
            abort(404, msg=u"操作失败")
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功"
        }
        return data
