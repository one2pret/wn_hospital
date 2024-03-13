# -*- coding: utf-8 -*-
# from odoo import http


# class WnHospital(http.Controller):
#     @http.route('/wn_hospital/wn_hospital', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wn_hospital/wn_hospital/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('wn_hospital.listing', {
#             'root': '/wn_hospital/wn_hospital',
#             'objects': http.request.env['wn_hospital.wn_hospital'].search([]),
#         })

#     @http.route('/wn_hospital/wn_hospital/objects/<model("wn_hospital.wn_hospital"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wn_hospital.object', {
#             'object': obj
#         })
