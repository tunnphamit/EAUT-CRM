
from odoo import fields, models, api

class EautCrmStage(models.Model):
    _name = 'eaut.career.center.stage'
    _description = 'EAUT CRM Stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence'
    
    fold = fields.Boolean(
        string="Folded in Kanban",
        help="This stage is folded (collapsed) in the Kanban view when empty.",
        default=False
    )

    sequence = fields.Integer(string="Sequence", default=10)
    name = fields.Char(string='Stage Name', required=True)
    description = fields.Text(string='Description')

    model_type = fields.Selection(
        [
            ('student', 'Student'),
            ('employer', 'Employer'),
        ],
        string='Belong to',
        required=True,
        default='student',
        tracking=True
    )
