# -*- coding: utf-8 -*-
# from odoo import http


# class SoCustomConfirmDate(http.Controller):
#     @http.route('/so_custom_confirm_date/so_custom_confirm_date/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/so_custom_confirm_date/so_custom_confirm_date/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('so_custom_confirm_date.listing', {
#             'root': '/so_custom_confirm_date/so_custom_confirm_date',
#             'objects': http.request.env['so_custom_confirm_date.so_custom_confirm_date'].search([]),
#         })

#     @http.route('/so_custom_confirm_date/so_custom_confirm_date/objects/<model("so_custom_confirm_date.so_custom_confirm_date"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('so_custom_confirm_date.object', {
#             'object': obj
#         })
