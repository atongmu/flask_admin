# -*- coding: utf-8 -*-
import base64
import imghdr
import os
import time

from flask_restful import Resource, reqparse, abort, marshal_with, fields
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from app.apis.api_constant import HTTP_OK, BASE_PATH, IMAGES_PATH, IMAGES_LINK
from app.models import ImageDefault
from app.utils.common import allowed_photo, md5

parse_base = reqparse.RequestParser()
parse_base.add_argument('page_no', type=int, required=True, help=u"请输入请求参数")
parse_base.add_argument('page_size', type=int, required=True, help=u"请输入请求参数")

banner_fields = {
    "id": fields.Integer,
    "url": fields.String,
    "path": fields.String
}
banner_page = {
    "has_next": fields.Boolean,
    "has_prev": fields.Boolean,
    "next_num": fields.Integer,
    "prev_num": fields.Integer,
    "pages": fields.Integer,
    "items": fields.List(fields.Nested(banner_fields)),
    "total": fields.Integer
}
single_image_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(banner_fields)
}


class ImagePageResource(Resource):
    """图片列表"""

    @marshal_with(single_image_fields)
    def get(self):
        args = parse_base.parse_args()
        page_no = args.get("page_no")
        page_size = args.get("page_size")
        image_default = ImageDefault.query.order_by(ImageDefault.id.desc()).paginate(page_no, page_size)
        data = {
            "status": HTTP_OK,
            "msg": u"操作成功",
            "data": image_default
        }
        return data
