
from odoo import fields, models, api

class EautCrmTag(models.Model):
    _name = 'eaut.career.center.tag'
    _description = 'Tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color', default=0)