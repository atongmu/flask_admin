# -*- coding: utf-8 -*-
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(use_native_unicode='utf8')
migrate = Migrate()
jwt = JWTManager()


def init_ext(app):
    # 跨域
    CORS(app, supports_credentials=True)
    # 数据库
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    from app.utils import auth_jwt
