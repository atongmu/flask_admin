# -*- coding: utf-8 -*-
from flask_restful import Api

from app.apis.system_poster.all_poster_api import PosterAllResource
from app.apis.system_poster.append_poster_api import PosterAppendResource
from app.apis.system_poster.remove_poster_api import PosterRemoveResource
from app.apis.system_poster.update_poster_api import PosterUpdateResource

system_poster_api = Api(prefix="/api/poster_api", catch_all_404s=True)

system_poster_api.add_resource(PosterAppendResource, "/poster_append")
system_poster_api.add_resource(PosterUpdateResource, "/poster_update")
system_poster_api.add_resource(PosterRemoveResource, "/poster_remove")
system_poster_api.add_resource(PosterAllResource, "/poster_all")
