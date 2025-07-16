
from odoo import fields, models, api

class EautCrmSupportTeam(models.Model):
    _name = 'eaut.career.center.support.team'
    _description = 'Support Team'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Support Team', required=True, tracking=True)
    description = fields.Text(string='Description')
    note = fields.Html(string="Note")
    leader_id = fields.Many2one(
        'res.partner',
        string='Team Leader',
        tracking=True,
        help='The leader of the support team.'
    )

    member_ids = fields.Many2many(
        'res.partner',
        'eaut_support_team_partner_rel',
        'team_id',
        'partner_id',
        string='Team Members'
    )
