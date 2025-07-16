
from odoo import models, fields, api

class EautCrmMouContract(models.Model):
    _name = 'eaut.career.center.mou.contract'
    _description = 'MOU Contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True, tracking=True)
    employer_id = fields.Many2one('eaut.career.center.employer', string='Employer', required=True, tracking=True)
    # Valid umtil
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    scope_of_cooperation = fields.Selection(
        selection=[
            ('internship', 'Thực tập'),
            ('sponsor', 'Tài trợ'),
            ('recruitment', 'Tuyển dụng'),
            ('other', 'Khác'),
        ],
        string='Scope of Cooperation',
        required=True,
        tracking=True
    )
    # Show when scope_of_cooperation is 'other'
    cooperation_details = fields.Text(string='Cooperation Details', tracking=True)
    
    # Contract file
    attached_file = fields.Binary(string='Attached File', attachment=True)
    attached_filename = fields.Char(string="Filename")
    
    note = fields.Html(string='Note')

    # def action_view_file(self):
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/web/content/%s?download=true' % (self.attached_file),
    #         'target': 'self',
    #     }