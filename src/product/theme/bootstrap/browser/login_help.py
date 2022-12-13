# -*- coding: utf-8 -*-
from Products.CMFPlone.browser.login.login_help import LoginHelpForm as lhf
from Products.CMFPlone.browser.login.login_help import RequestResetPassword as rrp
from Products.CMFPlone.browser.login.login_help import RequestUsername as ruser
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class RequestResetPassword(rrp):
    render = ViewPageTemplateFile('subform_render.pt')


class RequestUsername(ruser):
    render = ViewPageTemplateFile('subform_render.pt')


class LoginHelpForm(lhf):
    """"""

    def update(self):
        super(LoginHelpForm, self).update()
        subforms = []
        if self.can_reset_password():
            form = RequestResetPassword(None, self.request)
            form.update()
            subforms.append(form)
        if not self.use_email_as_login() and self.can_retrieve_username():
            form = RequestUsername(None, self.request)
            form.update()
            subforms.append(form)

        self.subforms = subforms
