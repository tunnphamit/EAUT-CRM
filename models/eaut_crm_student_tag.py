
from odoo import fields, models, api

class EautCrmStudentTag(models.Model):
    _name = 'eaut.crm.student.tag'
    _description = 'Student Tag'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Tag Name', required=True)
    color = fields.Integer(string='Color', default=0)