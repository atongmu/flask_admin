# -*- coding: utf-8 -*-
from flask_restful import Api
from app.apis.system_banner.append_banner_api import BannerAppendResource

system_banner_api = Api(prefix="/api/banner_api", catch_all_404s=True)

system_banner_api.add_resource(BannerAppendResource, "/banner_append")
