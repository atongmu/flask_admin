# -*- coding: utf-8 -*-
import os

HTTP_OK = 200

ACTION_LOGIN = "login"
ACTION_LOGOUT = "logout"

ACTION_INFO = "info"
ACTION_APPEND = "append"
ACTION_UPDATE = "update"
ACTION_DELETE = "delete"
ACTION_ALL = "all"
ACTION_PAGE = "page"
ACTION_STATUS = "status"
ACTION_COUNT = "count"

IMAGES_PATH = "app/static/images/server"
IMAGES_LINK = "/static/images/server"
BASE_PATH = os.path.abspath(os.path.dirname(__name__))
