
from odoo import models, fields, api

class EautCareerCenterMouContract(models.Model):
    _name = 'eaut.career.center.mou.contract'
    _description = 'MOU Contract'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True, tracking=True)
    employer_id = fields.Many2one('eaut.career.center.employer', string='Employer', required=True, tracking=True)
    # Valid umtil
    start_date = fields.Date(string='Start Date', required=True, tracking=True)
    end_date = fields.Date(string='End Date', required=True, tracking=True)
    # Scope of cooperation
    scope_ids = fields.Many2many(
        'eaut.career.center.mou.scope',
        'mou_contract_scope_rel',
        'contract_id',
        'scope_id',
        string='Scopes of Cooperation'
    )

    # Contract file
    attached_file = fields.Binary(string='Attached File', attachment=True)
    attached_filename = fields.Char(string="Filename")
    
    note = fields.Html(string='Note')
    storage_location = fields.Char(string='Storage Location', help="Nơi lưu trữ hợp đồng")
    signing_responsible = fields.Many2one(
        'res.users',
        string='Signing Responsible',
        help="Đơn vị phụ trách ký kết hợp đồng",
    )

    # def action_view_file(self):
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'url': '/web/content/%s?download=true' % (self.attached_file),
    #         'target': 'self',
    #     }