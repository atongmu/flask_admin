# -*- coding: utf-8 -*-
from flask_jwt_extended import create_access_token, jwt_refresh_token_required, get_jwt_identity, create_refresh_token
from flask_restful import Resource
from app.apis.api_constant import HTTP_OK


class AdminRefreshTokenResource(Resource):
    """刷新Token"""

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        ret = {
            'access_token': create_access_token(identity=current_user)
        }
        data = {
            "status": HTTP_OK,
            "msg": "获取成功",
            "data": ret
        }
        return data
