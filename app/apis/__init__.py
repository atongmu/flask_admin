from app.apis.system_admin import system_admin_api
from app.apis.system_banner import system_banner_api
from app.apis.system_config import system_config_api
from app.apis.system_image import system_image_api
from app.apis.system_poster import system_poster_api


def init_views_api(app):
    system_admin_api.init_app(app)
    system_banner_api.init_app(app)
    system_config_api.init_app(app)
    system_image_api.init_app(app)
    system_poster_api.init_app(app)
