
from odoo import fields, models, api, _
import re
from odoo.exceptions import ValidationError

class EautCrmStudent(models.Model):
    _name = 'eaut.crm.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # tracking=True -> Khi trường thay đổi, Odoo sẽ ghi lại lịch sử thay đổi vào Chatter
    code = fields.Char(string="Student Code", required=True, tracking=True)
    name = fields.Char(string='Full Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    photo = fields.Binary(string='Photo', attachment=True) # Ảnh đại diện
    note = fields.Html(string="Note")
    address = fields.Text(string='Address')

    # tag_ids = fields.Many2many('eaut.crm.student.tag', string='Tags')

    # Quan hệ Khoa, Khóa, Ngành
    faculty_ids = fields.Many2many(
        'eaut.crm.faculty',
        'student_faculty_rel',
        'student_id',
        'faculty_id',
        string='Faculties',
        tracking=True
    )
    major_ids = fields.Many2many(
        'eaut.crm.major',
        'student_major_rel',
        'student_id',
        'major_id',
        string='Majors',
        tracking=True
    )
    program_ids = fields.Many2many(
        'eaut.crm.program',
        'student_program_rel',
        'student_id',
        'program_id',
        string='Programs',
        tracking=True
    )

    # Tham chiếu đến Event
    event_ids = fields.Many2many('event.event', string='Participated Events')

    # Khóa học đã học
    slide_channel_ids = fields.Many2many('slide.channel', string="Participated Courses")

    # Ràng buộc Unique cho mã Sinh viên và Email
    _sql_constraints = [
        ('student_code_unique', 'unique(code)', 'Student Code must be unique!'),
        ('email_unique', 'unique(email)', 'Email must be unique!'),
    ]

    # # Quan hệ với Support Team
    support_team_id = fields.Many2one('eaut.crm.eaut_support_team', string='Support Team')

    # Quan hệ với Stage
    stage_id = fields.Many2one('eaut.crm.stage', string="Stage", tracking=True, index=True)

    # stage_id = fields.Many2one(
    #     'eaut.crm.stage',
    #     string="Stage",
    #     tracking=True,
    #     index=True,
    #     # domain="[('model_type', '=', 'student')]"
    # )

    # Validation

    # Email validation
    @api.constrains('email')
    def _check_email_format(self):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for rec in self:
            if rec.email and not re.match(email_pattern, rec.email):
                raise ValidationError(_("Email '%s' is not a valid email address!") % rec.email)
