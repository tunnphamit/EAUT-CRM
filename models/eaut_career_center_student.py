
from odoo import fields, models, api, _
import re
from odoo.exceptions import ValidationError

class EautCrmStudent(models.Model):
    _name = 'eaut.career.center.student'
    _description = 'Student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # tracking=True -> Khi trường thay đổi, Odoo sẽ ghi lại lịch sử thay đổi vào Chatter

    # Storage feature
    # active = fields.Boolean(default=True)
    code = fields.Char(string="Student Code", required=True, tracking=True)
    name = fields.Char(string='Full Name', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Phone', required=True, tracking=True)
    date_of_birth = fields.Date(string='Date of Birth')
    photo = fields.Binary(string='Photo', attachment=True) # Ảnh đại diện
    note = fields.Html(string="Note")
    address = fields.Text(string='Address')

    have_cv = fields.Boolean(string='Have CV', default=False)
    cv_link = fields.Char(string='CV Link')

    # Quan hệ Khoa, Khóa, Ngành
    faculty_id = fields.Many2one(
        'eaut.career.center.faculty',
        string='Faculty',
        tracking=True
    )

    major_id = fields.Many2one(
        'eaut.career.center.major',
        string='Major',
        tracking=True
    )
    
    program_id = fields.Many2one(
        'eaut.career.center.program',
        string='Program',
        tracking=True
    )

    # Tham chiếu đến Event
    event_ids = fields.Many2many('event.event', string='Participated Events')

    # Khóa học đã học
    slide_channel_ids = fields.Many2many('slide.channel', string="Participated Courses")

    # Quan hệ với Support Team
    # support_team_id = fields.Many2one('eaut.career.center.eaut_support_team', string='Support Team')

    # Quan hệ với Stage
    # stage_id = fields.Many2one('eaut.career.center.stage', string="Stage", tracking=True, index=True)
    stage_id = fields.Many2one(
        'eaut.career.center.stage',
        string="Stage",
        tracking=True,
        index=True,
        group_expand='_read_group_stage_ids',
        domain="[('model_type', '=', 'student')]"
    )
    tag_ids = fields.Many2many(
        'eaut.career.center.tag',
        'student_tag_rel',
        'student_id',
        'tag_id',
        string='Tags',
        tracking=True
    )

    # Override the _read_group_stage_ids method to filter stages by model_type
    # Hiện thị các stage thuộc model_type là 'student' kể cả khi không có student nào
    # trong stage đó
    @api.model
    def _read_group_stage_ids(self, stages, domain, order=None):
        return self.env['eaut.career.center.stage'].search(
            [('model_type', '=', 'student')],
            order=order or 'sequence'
        )
    
    # Ràng buộc Unique cho mã Sinh viên và Email
    _sql_constraints = [
        ('student_code_unique', 'unique(code)', 'Student Code must be unique!'),
        ('email_unique', 'unique(email)', 'Email must be unique!'),
    ]

    # Validation
    # Email validation
    @api.constrains('email')
    def _check_email_format(self):
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        for rec in self:
            if rec.email and not re.match(email_pattern, rec.email):
                raise ValidationError(_("Email '%s' is not a valid email address!") % rec.email)
