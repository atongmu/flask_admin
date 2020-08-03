# -*- coding: utf-8 -*-
import base64
import imghdr
import os
import time

from flask_restful import Resource, reqparse, abort
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from app.apis.api_constant import HTTP_OK, BASE_PATH, IMAGES_PATH, IMAGES_LINK
from app.models import ImageDefault
from app.utils.common import allowed_photo, md5

parse_base = reqparse.RequestParser()
parse_base.add_argument('file', type=FileStorage, location='files', help=u"请输入请求参数")
parse_base.add_argument('base64', help=u"请输入请求参数")


class ImageAppendResource(Resource):
    """图片注册"""

    def post(self):
        args = parse_base.parse_args()
        file_obj = args.get("file")
        base64_image = args.get("base64")
        # 图片文件上传
        if file_obj is not None:
            filename = file_obj.filename
            file_type = imghdr.what(file_obj)
            if not allowed_photo(file_type):
                abort(404, msg=u"请检查上传的图片类型，仅限于png、PNG、jpg、JPG、bmp")
            timestamp = md5(str(time.time()))
            new_file_name = timestamp + "." + (filename.rsplit('.', 1)[1])
            server_path = os.path.join(BASE_PATH, IMAGES_PATH)
            if not os.path.exists(server_path):
                os.makedirs(server_path)
            upload_path = os.path.join(server_path, secure_filename(new_file_name))
            image_path = os.path.join(IMAGES_LINK, secure_filename(new_file_name))
            file_obj.save(upload_path)
        elif base64_image is not None:
            img_data = base64.b64decode(base64_image)
            timestamp = md5(str(time.time()))
            new_file_name = timestamp + '.jpg'
            server_path = os.path.join(BASE_PATH, IMAGES_PATH)
            if not os.path.exists(server_path):
                os.makedirs(server_path)
            upload_path = os.path.join(server_path, secure_filename(new_file_name))
            image_path = os.path.join(IMAGES_LINK, secure_filename(new_file_name))
            with open(upload_path, 'wb') as f:
                f.write(img_data)
                f.close()
        image_default = ImageDefault()
        image_default.url = image_path
        image_default.path = upload_path
        if not image_default.is_save():
            abort(404, msg=u"图片注册失败")
        data = {
            "status": HTTP_OK,
            "msg": u"注册成功"
        }
        return data
