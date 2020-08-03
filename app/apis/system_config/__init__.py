# -*- coding: utf-8 -*-
from flask_restful import Api

from app.apis.system_config.all_config_api import ConfigAllResource
from app.apis.system_config.append_config_api import ConfigAppendResource
from app.apis.system_config.remve_config_api import ConfigRemoveResource
from app.apis.system_config.update_config_api import ConfigUpdateResource

system_config_api = Api(prefix="/api/config_api", catch_all_404s=True)

system_config_api.add_resource(ConfigAppendResource, "/config_append")
system_config_api.add_resource(ConfigUpdateResource, "/config_update")
system_config_api.add_resource(ConfigRemoveResource, "/config_remove")
system_config_api.add_resource(ConfigAllResource, "/config_all")
