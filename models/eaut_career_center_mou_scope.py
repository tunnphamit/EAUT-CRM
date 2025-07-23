
from odoo import models, fields, api

class EautCrmMouScope(models.Model):
    _name = 'eaut.career.center.mou.scope'
    _description = 'MOU Scope of Cooperation'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Scope name', required=True)
    color = fields.Integer(string='Color', default=0)
    