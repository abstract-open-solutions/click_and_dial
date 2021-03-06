# -*- encoding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Abstract
#    (<http://abstrat.it).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
from openerp import models, fields, api


class res_company(models.Model):
    _name = "res.company"
    _inherit = "res.company"

    voip_url = fields.Char(
        'Voip url',
        size=255,
        required=True,
        default=(
            'https://www.openvoip.it/click_and_dial.php?'
            'sender={sender}&dst={dst}&id_call_gr={id_call_gr}'
            '&verify={verify}'
        )
    )

    voip_debug = fields.Boolean(
        'Voip debug',
        default=False
    )

    @api.multi
    def set_default_voip_url(self, context):
        voip_url = (
            'https://www.openvoip.it/click_and_dial.php?'
            'sender={sender}&dst={dst}&id_call_gr={id_call_gr}'
            '&verify={verify}'
        )

        for company in self:
            if not company.voip_url:
                company.write({'voip_url': voip_url})
