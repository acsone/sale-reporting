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

from openerp import models, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.multi
    def action_open_sale_report_view(self):
        product_template = self.env['product.template']
        result = product_template.get_action_open_sale_report_view()
        result['domain'] = ("[('product_id','in',[" +
                            ','.join(map(str, self._ids)) + "])]")
        return result


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def get_action_open_sale_report_view(self):
        act_obj = self.env['ir.actions.act_window']
        mod_obj = self.env['ir.model.data']
        res_id = mod_obj.xmlid_to_res_id(
            'sale_report_static.act_open_model_sale_report_static_view',
            raise_if_not_found=True)
        result = act_obj.browse(res_id).read()[0]
        result['target'] = 'new'
        return result

    @api.multi
    def action_open_sale_report_view(self):
        product_ids = self.mapped('product_variant_ids.id')
        result = self.get_action_open_sale_report_view()
        result['domain'] = ("[('product_id','in',[" +
                            ','.join(map(str, product_ids)) + "])]")
        return result
