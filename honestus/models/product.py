# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


def is_not_empty(value):
    return value != "" and value


class ProductProductInherit(models.Model):
    _inherit = 'product.product'
    _rec_name = 'rec_name'

    @api.depends('name', 'honestus_code', 'default_code')
    def _compute_rec_name(self):
        for var in self:
            default_code = var.default_code if is_not_empty(var.default_code) else '-'
            code = var.honestus_code if is_not_empty(var.honestus_code) else default_code
            var.rec_name = f'[{code}] {var.name}'

    rec_name = fields.Char(compute='_compute_rec_name')
    honestus_code = fields.Char()
    honestus_price = fields.Float()
