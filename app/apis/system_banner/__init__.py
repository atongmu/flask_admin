# -*- coding: utf-8 -*-
from flask_restful import Api

from app.apis.system_banner.all_banner_api import BannerAllResource
from app.apis.system_banner.append_banner_api import BannerAppendResource
from app.apis.system_banner.remove_banner_api import BannerRemoveResource
from app.apis.system_banner.update_banner_api import BannerUpdateResource

system_banner_api = Api(prefix="/api/banner_api", catch_all_404s=True)

system_banner_api.add_resource(BannerAppendResource, "/banner_append")
system_banner_api.add_resource(BannerUpdateResource, "/banner_update")
system_banner_api.add_resource(BannerRemoveResource, "/banner_remove")
system_banner_api.add_resource(BannerAllResource, "/banner_all")
