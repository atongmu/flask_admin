# -*- coding: utf-8 -*-
from flask_restful import Api
from app.apis.system_image.append_image_api import ImageAppendResource
from app.apis.system_image.page_image_api import ImagePageResource
from app.apis.system_image.remove_image_api import ImageRemoveResource

system_image_api = Api(prefix="/api/image_api", catch_all_404s=True)

system_image_api.add_resource(ImageAppendResource, "/image_append")
system_image_api.add_resource(ImagePageResource, "/image_page")
system_image_api.add_resource(ImageRemoveResource, "/image_remove")
