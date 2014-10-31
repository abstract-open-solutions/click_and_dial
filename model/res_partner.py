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
from openerp import models, api
from ..click_and_dial import make_call


class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    @api.one
    def action_dial_phone(self, context):
        '''Function called by the button 'Dial' next to the 'phone' field
        in the partner address view'''
        make_call(self, self.phone)

    @api.one
    def action_dial_mobile(self, context):
        '''Function called by the button 'Dial' next to the 'mobile' field
        in the partner address view'''
        make_call(self, self.mobile)
