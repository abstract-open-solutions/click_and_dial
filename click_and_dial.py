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
import logging
import md5
import re
import sha
import urllib2

from openerp import exceptions
from openerp import _


logger = logging.getLogger(__name__)
_TEST = True


def reformat_number(number):
    x = re.compile(r'\D*', re.VERBOSE)
    return "".join(x.split(number))


def make_call(klass, erp_number):
    if erp_number:
        dst = reformat_number(erp_number)

        user = klass.env['res.users'].browse(klass.env.uid)
        if user.voip_id_call_gr:
            id_call_gr = user.voip_id_call_gr
        else:
            raise exceptions.Warning(
                _(u"Call failed, your user doesn't have a valid "
                  u"Call Group Id. \n"
                  u"Please, set your Call Group Id in you preferences")
            )

        if user.voip_user_number:
            sender = user.voip_user_number
        else:
            raise exceptions.Warning(
                _(u"Call failed, your user doesn't have a valid "
                  u"voip number. \n"
                  u"Please, set your voip number in you preferences")
            )

        if user.voip_password:
            secret = user.voip_password
        else:
            raise exceptions.Warning(
                _(u"Call failed, your user doesn't have a valid "
                  u"Voip user password. \n"
                  u"Please, set your Voip user password in you preferences")
            )

        verify = '%s%s%s%s' % (sender, dst, secret, id_call_gr)

        verify = md5.new(sha.new(verify).hexdigest()).hexdigest()

        if not _TEST:
            # TODO: uncomment this
            # make url configurable
            # handle exceptions

            # url_voip = (
            #     'https://www.openvoip.it/click_and_dial.php?'
            #     'sender=%s&dst=%s&id_call_gr=%s&verify=%s'
            # ) % (sender, dst, id_call_gr, verify)

            # response = urllib2.urlopen(url_voip).read()

            logger.debug(
                "Click and Dial response %s on url %s" % (response, url_voip)
            )
        else:
            logger.warning(
                "User {} calling {}".format(sender, erp_number)
            )

    return True
