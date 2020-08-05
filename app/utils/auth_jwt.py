# -*- coding: utf-8 -*-
from flask import jsonify
from app.ext import jwt


@jwt.expired_token_loader
def my_expired_token_callback():
    # 过期
    return jsonify({"status": 403, "message": "token过期"})


@jwt.invalid_token_loader
@jwt.unauthorized_loader
def my_unauthorized_loader(identy):
    dictInfo = "The has no token: %s" % identy
    print dictInfo
    return jsonify({"status": 401, "message": "请登录"})
