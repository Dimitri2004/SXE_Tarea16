# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api

class partner_chinese_stats(models.Model):
    _inherit="res_partner"
    f_nac=fields.Data("Fecha de nacimiento")
    edad=fields.Integer(string="Edad",readonly=True,compute="_calcular_edad",store=True)
    signo_chino=fields.Char(string="Signo Chino",readonly=True,compute="_calcular_chinada",store=True)


    @api.depends('f_nac')
    def _calcular_edad(self):
        for record in self:
            if record.f_nac:
                now=datetime.now()
                operacion=now-record.f_nac
                record.edad=operacion.year
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
                        signo = "Mono"
                    case 2:
                        signo = "Mono"
                    case 3:
                        signo=""
                    case 4:
                        signo=""
                    case 5:
                        signo=""
                    case 6:
                        signo=""
                    case 7:
                        signo=""
                    case 8:
                        signo=""
                    case 9:
                        signo=""
                    case 10:
                        signo=""
                    case 11:
                        signo=""
                    case 12:
                        singo=""





