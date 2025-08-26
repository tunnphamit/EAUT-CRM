from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class EautCareerCenterStudentRegistration(models.Model):
    _name = 'eaut.career.center.student.registration'
    _description = 'Student Registration'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True, tracking=True)
    student_id = fields.Many2one('eaut.career.center.student', string='Student', tracking=True)
    deadline = fields.Date(string='Deadline', tracking=True)
    assign_to = fields.Many2one('res.users', string='Assign To', tracking=True)
    description = fields.Text(string="Description")

    stage_id = fields.Many2one(
        'eaut.career.center.stage',
        string="Stage",
        tracking=True,
        index=True,
        group_expand='_read_group_stage_ids',
        domain="[('model_type', '=', 'student_registration')]"
    )

    # nhận từ form website
    form_student_email = fields.Char(string="Student Email (from form)", copy=False, index=True)
    form_student_code  = fields.Char(string="Student Code (from form)",  copy=False, index=True)

    @api.model_create_multi
    def create(self, vals_list):
        Student = self.env['eaut.career.center.student'].sudo()
        new_vals_list = []

        for vals in vals_list:
            vals = dict(vals)  # tránh sửa tham chiếu gốc
            if not vals.get('student_id'):
                email = (vals.get('form_student_email') or '').strip()
                code  = (vals.get('form_student_code')  or '').strip()

                # 1) tìm Student đã có
                student = Student.browse()
                if code:
                    student = Student.search([('code', '=', code)], limit=1)
                if not student and email:
                    student = Student.search([('email', '=', email)], limit=1)

                # 2) nếu chưa có → tạo mới (chỉ khi có ÍT NHẤT 1 trong 2: email/code)
                if not student and (email or code):
                    # tên SV: lấy từ Title của registration (ảnh chụp của bạn là tên người)
                    student_name = (vals.get('name') or '').strip() or _('Unnamed')

                    # LƯU Ý: model Student đang đặt email & code là required=True.
                    # → để tạo được khi thiếu 1 trong 2, ta xử lý sau:
                    student_vals = {
                        'name': student_name,
                        'email': email or False,
                        'code': code or False,
                    }
                    # Nếu thiếu code, để Student model tự cấp từ sequence (ở bước 2 phía dưới)
                    # Nếu thiếu email, bạn CÓ THỂ đặt tạm placeholder duy nhất theo code:
                    if not student_vals['email'] and student_vals['code']:
                        student_vals['email'] = f"no-email+{student_vals['code']}@eaut.local"

                    # Tạo sinh viên (sudo để không vướng ACL của portal/public)
                    student = Student.create(student_vals)

                if student:
                    vals['student_id'] = student.id

            new_vals_list.append(vals)

        records = super(EautCareerCenterStudentRegistration, self).create(new_vals_list)
        return records

    @api.model
    def _read_group_stage_ids(self, stages, domain, order=None):
        return self.env['eaut.career.center.stage'].search(
            [('model_type', '=', 'student_registration')],
            order=order or 'sequence'
        )
