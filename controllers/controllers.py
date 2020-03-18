# -*- coding: utf-8 -*-
from odoo import http

# class VitBudgetLocationFilter(http.Controller):
#     @http.route('/vit_budget_location_filter/vit_budget_location_filter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_budget_location_filter/vit_budget_location_filter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_budget_location_filter.listing', {
#             'root': '/vit_budget_location_filter/vit_budget_location_filter',
#             'objects': http.request.env['vit_budget_location_filter.vit_budget_location_filter'].search([]),
#         })

#     @http.route('/vit_budget_location_filter/vit_budget_location_filter/objects/<model("vit_budget_location_filter.vit_budget_location_filter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_budget_location_filter.object', {
#             'object': obj
#         })