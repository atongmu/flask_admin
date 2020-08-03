# -*- coding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with
from app.apis.api_constant import HTTP_OK
from app.models import PostersDefault

poster_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "url": fields.String,
    "desc": fields.String,
}
single_poster_fields = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.List(fields.Nested(poster_fields))
}


class PosterAllResource(Resource):
    """广告列表"""

    @marshal_with(single_poster_fields)
    def get(self):
        poster_default = PostersDefault.query.all()

        data = {
            "status": HTTP_OK,
            "msg": u"操作成功",
            "data": poster_default
        }
        return data
