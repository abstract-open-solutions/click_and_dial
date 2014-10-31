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

from openerp import models, fields, api, _
from openerp import netsvc

import urllib2
import md5
import sha
import re


def reformat_number(number):
    x = re.compile(r'\D*', re.VERBOSE)
    return "".join(x.split(number))


def make_call(self, cr, uid, erp_number):
    logger = netsvc.Logger()
    if erp_number:
        dst = reformat_number(erp_number)

        user = self.pool.get('res.users').browse(cr, uid, uid)
        if user.id_call_gr:
            id_call_gr = user.id_call_gr
        else:
            raise osv.except_osv(
                _('Errore :'),
                _(u'Settare il call id per l\'utente.')
            )

        if user.internal_number:
            sender = user.internal_number
        else:
            raise osv.except_osv(
                _('Errore :'),
                _(u'L\'utente non ha nessun numero associato.')
            )

        if user.secret_key_password:
            secret = user.secret_key_password
        else:
            raise osv.except_osv(
                _('Errore :'),
                _(u'Settare la password per accedere '
                    'al servizio click and dial.')
            )

        verify = '%s%s%s%s' % (sender, dst, secret, id_call_gr)

        verify = md5.new(sha.new(verify).hexdigest()).hexdigest()

        url_voip = (
            'https://www.openvoip.it/click_and_dial.php?'
            'sender=%s&dst=%s&id_call_gr=%s&verify=%s'
        ) % (sender, dst, id_call_gr, verify)

        response = urllib2.urlopen(url_voip).read()

        logger.notifyChannel(
            'arpes_base',
            netsvc.LOG_INFO,
            "Click and Dial response %s on url %s" % (response, url_voip)
        )

    return True


# class res_partner_address(models.Model):
#     _name = "res.partner.address"
#     _inherit = "res.partner.address"

#     def action_dial_phone(self, cr, uid, ids, context=None):
#         '''Function called by the button 'Dial' next to the 'phone' field
#         in the partner address view'''

#         erp_number = self.read(
#             cr, uid, ids, ['phone'], context=context
#         )[0]['phone']
#         return make_call(self, cr, uid, erp_number)

#     def action_dial_mobile(self, cr, uid, ids, context=None):
#         '''Function called by the button 'Dial' next to the 'mobile' field
#         in the partner address view'''

#         erp_number = self.read(
#             cr, uid, ids, ['mobile'], context=context
#         )[0]['mobile']
#         return make_call(self, cr, uid, erp_number)


# class res_partner_contact(models.Model):
#     _name = "res.partner.contact"
#     _inherit = "res.partner.contact"

#     def action_dial_phone(self, cr, uid, ids, context=None):
#         '''Function called by the button 'Dial' next to the 'phone' field
#         in the partner address view'''

#         erp_number = self.read(
#             cr, uid, ids, ['telephone'], context=context
#         )[0]['telephone']
#         return make_call(self, cr, uid, erp_number)

#     def action_dial_mobile(self, cr, uid, ids, context=None):
#         '''Function called by the button 'Dial' next to the 'mobile' field
#         in the partner address view'''

#         erp_number = self.read(
#             cr, uid, ids, ['mobile'], context=context
#         )[0]['mobile']
#         return make_call(self, cr, uid, erp_number)
