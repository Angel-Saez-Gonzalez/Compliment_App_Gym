# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class complimentApp(models.Model):
    _inherit = 'gym_app.client_model'

    user = fields.Many2one("res.users",string="User")
    

    def clean_Tasks(self):
        if self.user != self.env.user:
            raise ValidationError("The user is not the responsible")
        else:
            return super(complimentApp,self).clean_Tasks()


    