# from openerp import models, fields, api, _
from openerp.osv import fields, osv


# Specific paremeters for each user
class res_users(osv.osv):
    _name = "res.users"
    _inherit = "res.users"

    _columns = {
        # formerly id_call_gr
        "voip_id_call_gr": fields.char('Id Call Group', size=6),
        # formerly internal_number
        "voip_internal_number": fields.char('Voip number', size=15),
        # formerly secret_key_password
        "voip_password": fields.char('Voip user password', size=64),
    }
