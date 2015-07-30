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

{
    "name": "Sale report",
    "version": "0.1",
    'author': "Acsone, Odoo Community Association (OCA)",
    "category": "Other",
    "website": "http://www.acsone.eu",
    'summary': "",
    "depends": ['sale',
                # 'materialized_sql_view',
                ],
    "data": ["views/sale_report_static.xml",
             "views/product_view.xml",
             ],
    "license": "AGPL-3",
    "installable": True,
    "application": False,
}
