# -*- coding: utf-8 -*-
# from odoo import http


# class SchoolMgmt(http.Controller):
#     @http.route('/school_mgmt/school_mgmt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school_mgmt/school_mgmt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school_mgmt.listing', {
#             'root': '/school_mgmt/school_mgmt',
#             'objects': http.request.env['school_mgmt.school_mgmt'].search([]),
#         })

#     @http.route('/school_mgmt/school_mgmt/objects/<model("school_mgmt.school_mgmt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school_mgmt.object', {
#             'object': obj
#         })

