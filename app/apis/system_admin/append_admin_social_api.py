from flask_restful import Resource, reqparse, abort
from app.apis.api_constant import HTTP_OK
from app.apis.system_admin.admin_utils import get_admin
from app.ext import multi_auth
from app.models import Managers, SocialAccount

parse_base = reqparse.RequestParser()
parse_base.add_argument("identity_type", type=str, required=True, help="请输入请求参数")
parse_base.add_argument("identifier", type=str, required=True, help="请输入请求参数")
parse_base.add_argument("credential", type=str, required=True, help="请输入请求参数")


class AdminSocialAppendResource(Resource):
    """用户第三方注册"""

    def post(self):
        args = parse_base.parse_args()
        identity_type = args.get("identity_type")
        identifier = args.get("identifier")
        credential = args.get("credential")
        manager = get_admin(identifier)
        if manager:
            abort(404, msg="用户已存在")
        new_manager = Managers()
        new_manager.users_name = credential
        new_manager.password = '888888'
        if not new_manager.is_save():
            abort(404, msg="用户注册失败")

        social_account = SocialAccount()
        social_account.identity_type = identity_type
        social_account.identifier = identifier
        social_account.credential = credential
        social_account.u_id = manager.id
        if not social_account.is_save():
            abort(404, msg="用户注册失败")

        data = {
            "status": HTTP_OK,
            "msg": u"注册成功"
        }
        return data
