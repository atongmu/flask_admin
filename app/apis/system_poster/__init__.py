# -*- coding: utf-8 -*-
from flask_restful import Api
from app.apis.system_poster.append_poster_api import PosterAppendResource

system_poster_api = Api(prefix="/api/poster_api", catch_all_404s=True)

system_poster_api.add_resource(PosterAppendResource, "/poster_append")
