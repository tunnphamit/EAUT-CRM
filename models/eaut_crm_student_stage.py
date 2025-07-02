
from odoo import fields, models, api

class EautCrmStudentStage(models.Model):
    _name = 'eaut.crm.student.stage'
    _description = 'Student Stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Stage Name', required=True, tracking=True)
    sequence = fields.Integer(string='Sequence', default=10)