# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Honestus Task',
    'version': '1.0',
    'category': 'Honestus',
    'sequence': 95,
    'summary': 'Honestus Task',
    'author': "Ana Zurabashvili",
    'depends': ['website',
                'product_margin',
                'sale', 'sale_management',
                'website_payment'
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/account_form.xml',
        'views/product.xml',
        'views/product_reports.xml',
        'views/honestus_report.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
