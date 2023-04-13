from odoo.exceptions import UserError
from odoo.http import request
from odoo import _
from odoo.addons.web.controllers.home import SIGN_UP_REQUEST_PARAMS
from odoo.addons.web.controllers.home import Home


class AuthSignupHomeInherit(Home):
    def get_auth_signup_qcontext(self):
        """ Shared helper returning the rendering context for signup and reset password """
        SIGN_UP_REQUEST_PARAMS.add('mobile')
        qcontext = {k: v for (k, v) in request.params.items() if k in SIGN_UP_REQUEST_PARAMS}

        qcontext.update(self.get_auth_signup_config())

        if not qcontext.get('token') and request.session.get('auth_signup_token'):
            qcontext['token'] = request.session.get('auth_signup_token')
        if qcontext.get('token'):
            try:
                # retrieve the user info (name, login or email) corresponding to a signup token
                token_infos = request.env['res.partner'].sudo().signup_retrieve_info(qcontext.get('token'))
                for k, v in token_infos.items():
                    qcontext.setdefault(k, v)
            except:
                qcontext['error'] = _("Invalid signup token")
                qcontext['invalid_token'] = True
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
