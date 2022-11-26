# -*- coding: utf-8 -*-
# from odoo import http


# class TestingNewFolder(http.Controller):
#     @http.route('/testing_new_folder/testing_new_folder/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testing_new_folder/testing_new_folder/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testing_new_folder.listing', {
#             'root': '/testing_new_folder/testing_new_folder',
#             'objects': http.request.env['testing_new_folder.testing_new_folder'].search([]),
#         })

#     @http.route('/testing_new_folder/testing_new_folder/objects/<model("testing_new_folder.testing_new_folder"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testing_new_folder.object', {
#             'object': obj
#         })
