
from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
    contract_file = fields.Binary(string='Contract file', attachment=True)
    contract_filename = fields.Char(string="Contract file name", tracking=True)
    
    note = fields.Html(string='Note')
    storage_location = fields.Char(string='Storage Location', help="Nơi lưu trữ hợp đồng")
    signing_responsible = fields.Many2one(
        'res.users',
        string='Signing Responsible',
        help="Đơn vị phụ trách ký kết hợp đồng",
    )

    @api.constrains('attached_filename')
    def _check_only_pdf(self):
        for record in self:
            if record.attached_filename and not record.attached_filename.lower().endswith('.pdf'):
                raise ValidationError("Hợp đồng phải là định dạng PDF (.pdf)")