# -*- coding: utf-8 -*-
from odoo import fields, models, api

"""
I was using abstract model instead of models.
abstract model is not directly associated with any database table 
we do not need to have this table in database.
but we cant see form and tree 

abstract model to write a report if the data you need to display
in the report comes from multiple models. 
"""


class HonestusReport(models.Model):
    _name = "honestus.report"
    _description = "Honestus Analysis Report"
    _auto = False

    product_id = fields.Many2one('product.product', 'Product Variant',
                                 readonly=True)
    partner_id = fields.Many2one('res.partner', 'Customer',
                                 readonly=True)
    order_id = fields.Many2one('sale.order', 'Order #',
                               readonly=True)
    name = fields.Char('Order Reference', readonly=True)
    default_code = fields.Char()
    honestus_code = fields.Char()
    price_unit = fields.Float()
    honestus_price = fields.Float()
    standard_price = fields.Float('cost')
    margin = fields.Float()

    # todo
    # standard_price = fields.Float('standard_price')
    #
    # @api.depends_context('company')
    # @api.depends('product_variant_ids', 'product_variant_ids.standard_price')
    # def _compute_standard_price(self):
    #     # Depends on force_company context because standard_price is company_dependent
    #     # on the product_product
    #     unique_variants = self.filtered(lambda template: len(template.product_variant_ids) == 1)
    #     for template in unique_variants:
    #         template.standard_price = template.product_variant_ids.standard_price
    #     for template in (self - unique_variants):
    #         template.standard_price = 0.0

    """
            if line.price_unit:
                margin = (price_unit - standard_price) / line.price_unit
            elif line.honestus_code:
                margin = (honestus_code - standard_price) / line.honestus_code
            else:
                margin = 0
     """

    def _select(self):
        select_ = f"""
            MIN(l.id)        AS id,
            l.product_id     AS product_id,
            s.name           AS name,
            s.partner_id     AS partner_id,
            s.id             AS order_id,
            p.honestus_price AS honestus_price,
            p.honestus_code  AS honestus_code,
            l.price_unit     AS price_unit,
            p.default_code   AS default_code,
            l.price_total    AS price_total,
            SUM(l.price_unit - {self._case_value_or_one('l.price_total')}
            / {self._case_value_or_one('l.price_unit')}) AS margin
            """
        return select_

    def _case_value_or_one(self, value):
        return f"""CASE COALESCE({value}, 0) 
        WHEN 0 THEN 1.0 ELSE {value} END"""

    def _from(self):
        return """
            sale_order_line l
            LEFT JOIN sale_order s ON s.id = l.order_id
            JOIN res_partner partner ON s.partner_id = partner.id
            LEFT JOIN product_product p ON l.product_id = p.id
            """

    def _where(self):
        return """l.product_id IS NOT Null"""

    def _group_by(self):
        return """
        s.id,
        l.product_id,
        l.order_id,
        s.name,
        s.partner_id,
        p.honestus_price,
        p.honestus_code,
        p.default_code,
        l.price_unit,
        l.price_total
        """

    def _query(self):
        return f"""
            SELECT {self._select()}
            FROM {self._from()}
            WHERE {self._where()}
            GROUP BY {self._group_by()}
        """

    @property
    def _table_query(self):
        return self._query()
