# -*- coding: utf-8 -*-
{
    'name': "Click and dial",
    'version': "1.0",
    'author': 'Abstract',
    'website': 'http://www.abstract.it',
    'category': '',
    'description': """Click and dial for openvoip.it

This module allow to make a call directly from odoo by clicking
on 'Dial' button near the telephone field in contact and partner models.
""",
    'license': 'AGPL-3',
    'depends': [
        'base'
    ],
    'data': [
        'view/res_users.xml',
        # 'data/odoo_reset.xml',
        # 'data/res_company.xml',

        # 'view/partner_view.xml'
    ],
    'active': False,
    'installable': True
}
