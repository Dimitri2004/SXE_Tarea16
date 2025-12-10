# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class fidelizacion_clientes(models.Model):
#     _name = 'fidelizacion_clientes.fidelizacion_clientes'
#     _description = 'fidelizacion_clientes.fidelizacion_clientes'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class fidelizacion_clientes(models.Model):
    _inherit = 'res.partner'

    c_socio=fields.Char(string="Codigo de socio")
    n_fidelidad=fields.Char(string="Nivel de fidelidad", readonly=True,compute="_calcular_fidelidad")

    @api.depends('c_socio')
    def _calcular_fidelidad(self):
        for record in self:
            if record.c_socio:
                if record.c_socio.startswith("G"):
                    record.n_fidelidad="Nivel GOLD"
                else :
                    record.n_fidelidad="Nivel PREMIUM"
            else:
                record.n_fidelidad="Nivel ESTANDAR"