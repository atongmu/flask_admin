# -*- coding: utf-8 -*-
from flask_restful import Api

from app.apis.system_admin.get_admin_api import AdminInfoResource
from app.apis.system_admin.token_admin_api import AdminTokenResource
from app.apis.system_admin.token_refresh_admin_api import AdminRefreshTokenResource

system_admin_api = Api(prefix="/api/manager_api", catch_all_404s=True)

system_admin_api.add_resource(AdminTokenResource, "/manager_token")
system_admin_api.add_resource(AdminRefreshTokenResource, "/manager_refresh_token")
system_admin_api.add_resource(AdminInfoResource, "/manager_info")
