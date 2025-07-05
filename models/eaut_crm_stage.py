
from odoo import fields, models, api

class EautCrmStage(models.Model):
    _name = 'eaut.crm.stage'
    _description = 'EAUT CRM Stage'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'sequence'
    # _fold_name = 'fold'

    sequence = fields.Integer(default=10)
    # fold = fields.Boolean(string="Folded in Kanban", help="This stage is folded in the kanban view.", default=False)
    name = fields.Char(string='Stage Name', required=True)
    description = fields.Text(string='Description')
