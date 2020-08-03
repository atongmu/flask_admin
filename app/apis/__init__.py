from app.apis.system_admin import system_admin_api


def init_views_api(app):
    system_admin_api.init_app(app)
