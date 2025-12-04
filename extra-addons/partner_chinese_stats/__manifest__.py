# -*- coding: utf-8 -*-
{
    'name': "partner_chinese_stats",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Este modulo extiende el modelo res_partner añadiendo 3 campos de contactos:
-Fecha
-Edad(calculada automaticamente)
-Signo del horoscopo chino(calculado automaticamente)
    """,

    'author': "Empleador sufridor",
    'website': "https://www.nocobrolosuficiente.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','contacts'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

