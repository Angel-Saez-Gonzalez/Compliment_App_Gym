# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class complimentApp(models.Model):
    _inherit = 'gym_app.client_model'

    user = fields.Many2one("res.users", string="User")
    state = fields.Selection(
        selection=[('notUser', 'Draft'), ('isUser', 'Confirmed')], default="notUser")
    hide_action_buttons = fields.Boolean(
        'Hide Action Buttons', compute='_compute_hide_action_buttons')

    def clean_Tasks(self):
        if self.user != self.env.user:
            raise ValidationError("The user is not the responsible")
        else:
            return super(complimentApp, self).clean_Tasks()

    @api.depends("user")
    def confUser(self):
        if self.user != self.env.user:
            self.state = "notUser"
            raise ValidationError("Yo are not the user")
        else:
            self.state = "isUser"

    @api.depends("state")
    def _compute_hide_action_buttons(self):
        if self.state == 'isUser':
            # Show Create/Edit buttons on draft
            self.hide_action_buttons = False
        elif self.state == 'notUser':
            # Hide Create/Edit buttons if order is done
            self.hide_action_buttons = True
