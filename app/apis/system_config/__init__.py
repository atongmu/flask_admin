# -*- coding: utf-8 -*-
from flask_restful import Api
from app.apis.system_config.append_config_api import ConfigAppendResource

system_config_api = Api(prefix="/api/config_api", catch_all_404s=True)

system_config_api.add_resource(ConfigAppendResource, "/config_append")
