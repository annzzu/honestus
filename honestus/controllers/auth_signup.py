from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError
from odoo.http import request
from odoo import _


class AuthSignupHomeInherit(AuthSignupHome):
    def get_auth_signup_qcontext(self):
        """had different solution, it is much easy to read and understand"""
        qcontext = super().get_auth_signup_qcontext()
        qcontext['mobile'] = request.params.get('mobile')
        return qcontext

    def _prepare_signup_values(self, qcontext):
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password', 'mobile')}
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '')
        if lang in supported_lang_codes:
            values['lang'] = lang
        return values
