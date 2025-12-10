# -*- coding: utf-8 -*-
# from odoo import http


# class FidelizacionClientes(http.Controller):
#     @http.route('/fidelizacion_clientes/fidelizacion_clientes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fidelizacion_clientes/fidelizacion_clientes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('fidelizacion_clientes.listing', {
#             'root': '/fidelizacion_clientes/fidelizacion_clientes',
#             'objects': http.request.env['fidelizacion_clientes.fidelizacion_clientes'].search([]),
#         })

#     @http.route('/fidelizacion_clientes/fidelizacion_clientes/objects/<model("fidelizacion_clientes.fidelizacion_clientes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fidelizacion_clientes.object', {
#             'object': obj
#         })

