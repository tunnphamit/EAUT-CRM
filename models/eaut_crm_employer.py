
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EautCrmEmployer(models.Model):
    _name = 'eaut.crm.employer'
    _description = 'Employer'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Company Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    website = fields.Char(string='Website')
    address = fields.Text(string='Address')
    photo = fields.Binary(string='Photo', attachment=True) # Ảnh đại diện
    note = fields.Html(string="Note")

    # Relationship with Students
    # Danh sách sinh viên đã đăng ký với nhà tuyển dụng
    student_ids = fields.Many2many(
        'eaut.crm.student',
        'employer_student_rel',
        'employer_id',
        'student_id',
        string='Students',
        tracking=True
    )

    # Quan hệ với Stage
    stage_id = fields.Many2one('eaut.crm.stage', string="Stage", tracking=True, index=True)

    # Relationship with Tags
    # tag_ids = fields.Many2many(
    #     'eaut.crm.tag',
    #     'student_tag_rel',
    #     'student_id',
    #     'tag_id',
    #     string='Tags',
    #     tracking=True
    # )

    # Unique constraint for email
    _sql_constraints = [
        ('email_unique', 'unique(email)', 'Email must be unique!'),
    ]