# -*- coding: utf-8 -*-
# from odoo import http


# class ComplimentApp(http.Controller):
#     @http.route('/compliment_app/compliment_app/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/compliment_app/compliment_app/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('compliment_app.listing', {
#             'root': '/compliment_app/compliment_app',
#             'objects': http.request.env['compliment_app.compliment_app'].search([]),
#         })

#     @http.route('/compliment_app/compliment_app/objects/<model("compliment_app.compliment_app"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('compliment_app.object', {
#             'object': obj
#         })
