
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EautCareerCenterEmployer(models.Model):
    _name = 'eaut.career.center.employer'
    _description = 'Employer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Company Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    website = fields.Char(string='Website')
    address = fields.Text(string='Address')
    photo = fields.Binary(string='Photo', attachment=True) # Ảnh đại diện
    tax_code = fields.Char(string='Tax Code', tracking=True)
    note = fields.Html(string="Note")

    # Industry
    industry = fields.Char(string='Industry', tracking=True)
    number_of_employees = fields.Integer(string='Number of Employees')
    
    # Contact Information
    contact_name = fields.Char(string='Contact Name')
    contact_email = fields.Char(string='Contact Email')
    contact_phone = fields.Char(string='Contact Phone')

    # Event
    event_ids = fields.Many2many('event.event', string='Participated Events')

    # MOU information
    mou_contract_ids = fields.One2many(
        'eaut.career.center.mou.contract',
        'employer_id',
        string='Hợp đồng MOU'
    )
    mou_contract_counter = fields.Integer(
        string='MOU Contract Count',
        compute='_compute_mou_contract_counter',
    )

    # Relationship with Students
    # Danh sách sinh viên đã đăng ký với nhà tuyển dụng
    student_ids = fields.Many2many(
        'eaut.career.center.student',
        'employer_student_rel',
        'employer_id',
        'student_id',
        string='Students',
    )

    # Quan hệ với Stage
    stage_id = fields.Many2one(
        'eaut.career.center.stage',
        string="Stage",
        tracking=True,
        index=True,
        group_expand='_read_group_stage_ids',
        domain="[('model_type', '=', 'employer')]"
    )

    # Relationship with Tags
    tag_ids = fields.Many2many(
        'eaut.career.center.tag',
        'employer_tag_rel',
        'employer_id',
        'tag_id',
        string='Tags'
    )

    # Smart buttons
    def action_view_mou_contract(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'MOU Contracts',
            'res_model': 'eaut.career.center.mou.contract',
            'view_mode': 'list,form',
            'domain': [('employer_id', '=', self.id)],
            'context': {'default_employer_id': self.id},
        }
    
    def _compute_mou_contract_counter(self):
        for employer in self:
            employer.mou_contract_counter = len(employer.mou_contract_ids)

    # Unique constraint for email
    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Email must be unique!'),
    ]

    # Override the _read_group_stage_ids method to filter stages by model_type
    # Hiện thị các stage thuộc model_type là 'student' kể cả khi không có student nào
    # trong stage đó
    @api.model
    def _read_group_stage_ids(self, stages, domain, order=None):
        return self.env['eaut.career.center.stage'].search(
            [('model_type', '=', 'employer')],
            order=order or 'sequence'
        )