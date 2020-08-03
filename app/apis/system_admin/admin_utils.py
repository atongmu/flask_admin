# -*- coding: utf-8 -*-
from app.models import Managers, SocialAccount


def get_admin(admin_ident):
    admin_one = Managers.query.get(admin_ident)
    if admin_one:
        return admin_one

    admin_one = Managers.query.filter(Managers.is_show == True,
                                      Managers.users_name == admin_ident).first()
    if admin_one:
        return admin_one

    social_account = SocialAccount.query.filter(SocialAccount.identifier == admin_ident).first()
    admin_one = Managers.query.get(social_account.u_id)
    if admin_one:
        return admin_one

    return None
