# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class partner_chinese_stats(models.Model):

    _inherit = 'res.partner'

    f_nac=fields.Date("Fecha de nacimiento")
    edad=fields.Integer(string="Edad",readonly=True,compute="_calcular_edad",store=True)
    signo_chino=fields.Char(string="Signo Chino",readonly=True,compute="_calcular_chinada",store=True)


    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                now=datetime.now().year
                operacion=now-record.f_nac.year
                record.edad=operacion
            else:
                record.edad=200
    @api.depends('f_nac')
    def _calcular_chinada(self):
        for record in self:
            if record.f_nac:
                signo="sin asignar"
                resto=record.f_nac.year%12
                match(resto):
                    case 0:
                        signo="Mono"
                    case 1:
                        signo ="Gallo"
                    case 2:
                        signo ="Perro"
                    case 3:
                        signo="Cerdo"
                    case 4:
                        signo="Rata"
                    case 5:
                        signo="Buey"
                    case 6:
                        signo="Tigre"
                    case 7:
                        signo="Conejo"
                    case 8:
                        signo="Dragon"
                    case 9:
                        signo="Serpiente"
                    case 10:
                        signo="Caballo"
                    case 11:
                        signo="Cabra"
                record.signo_chino=signo







