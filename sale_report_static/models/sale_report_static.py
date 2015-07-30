# -*- coding: utf-8 -*-
##############################################################################
#
#    Authors: Laurent Mignon
#    Copyright (c) 2015 Acsone SA/NV (http://www.acsone.eu)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.tools.sql import drop_view_if_exists
import openerp.addons.decimal_precision as dp
from openerp import models, fields


class SaleReportStatic(models.Model):
    _name = 'sale.report.static'
    _description = u"Total Sales"
    _auto = False
    _order = 'product_id'

    def init(self, cr):
        drop_view_if_exists(cr, 'sale_report_static')
        cr.execute("""
    create or replace view sale_report_static as (
with sale_count as (
 select
    pp.id as product_id,
    sum(sol.product_uom_qty) as qty,
    so.date_order
 from product_product pp
 join sale_order_line sol on pp.id = sol.product_id
 join sale_order so on so.id = sol.order_id
 group by pp.id, so.date_order
)
select
  pp.id,
  pp.id as product_id,
  COALESCE((select
      sum(sc.qty)
   from
       sale_count sc
   where
       sc.product_id = pp.id
       and sc.date_order > CURRENT_DATE
  ), 0) as total_sale_today,
  COALESCE((select
      sum(sc.qty)
   from
       sale_count sc
   where
       sc.product_id = pp.id
       and sc.date_order > CURRENT_DATE - INTERVAL '1 days'
  ), 0) as total_sale_last_day,
  COALESCE((select
      sum(sc.qty)
   from
       sale_count sc
   where
       sc.product_id = pp.id
       and sc.date_order > CURRENT_DATE - INTERVAL '1 weeks'
  ), 0) as total_sale_week,
  COALESCE((select
      sum(sc.qty)
   from
       sale_count sc
   where
       sc.product_id = pp.id
       and sc.date_order > CURRENT_DATE - INTERVAL '2 weeks'
  ), 0) as total_sale_two_weeks,
  COALESCE((select
      sum(sc.qty)
   from
       sale_count sc
   where
       sc.product_id = pp.id
       and sc.date_order > CURRENT_DATE - INTERVAL '1 months'
  ), 0) as total_sale_month,
  COALESCE((select
      sum(sc.qty)
   from
       sale_count sc
    where
        sc.product_id = pp.id
  ), 0) as total_sale
from product_product pp
where pp.active
order by pp.id
            )""")

    total_sale_today = fields.Float(
        'Total Today', readonly=True,
        digits_compute=dp.get_precision('Product UoS'))
    total_sale_last_day = fields.Float(
        'Total last day', readonly=True,
        digits_compute=dp.get_precision('Product UoS'))
    total_sale_week = fields.Float(
        'Total Week', readonly=True,
        digits_compute=dp.get_precision('Product UoS'))
    total_sale_two_weeks = fields.Float(
        'Total Two weeks', readonly=True,
        digits_compute=dp.get_precision('Product UoS'))
    total_sale_month = fields.Float(
        'Total Month', readonly=True,
        digits_compute=dp.get_precision('Product UoS'))
    total_sale = fields.Float(
        'Total', readonly=True,
        digits_compute=dp.get_precision('Product UoS'))
    product_id = fields.Many2one(
        comodel_name='product.product', string='Product', readonly=True)
