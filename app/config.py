# -*- coding: utf-8 -*-

def get_db_url(dbinfo):
    engine = dbinfo.get('ENGINE') or 'sqlite'
    driver = dbinfo.get('DRIVER') or 'sqlite'
    user = dbinfo.get('USER') or 'sqlite'
    password = dbinfo.get('PASSWORD') or ''
    host = dbinfo.get('HOST') or ''
    port = dbinfo.get('PORT') or ''
    name = dbinfo.get('NAME') or ''
    return '{}+{}://{}:{}@{}:{}/{}'.format(engine, driver, user, password, host, port, name)


class Config:
    DEBUG = False
    TESTING = False
    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'
    JWT_SECRET_KEY = '2ku0Vm1XCR9OGW6c'
    JWT_HEADER_TYPE = 'Token'
    JWT_ACCESS_TOKEN_EXPIRES = 1000
    SECRET_KEY = '2ku0Vm1XCR9OGW6c'


class DevelopmentConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "1234",
        "HOST": "127.0.0.1",
        "PORT": "3309",
        "NAME": "admin"
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True


class DefaultConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "zhangAI000829",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "NAME": "flask_cims"
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DefaultConfig
}
