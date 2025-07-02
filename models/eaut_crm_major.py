
from odoo import fields, models

class EautCrmMajor(models.Model):
    _name = 'eaut.crm.major'
    _description = 'Major' # Ngành
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Mã ngành (unique)
    code = fields.Char(string='Major code', required=True, tracking=True)

    # Tên ngành
    name = fields.Char(string='Major name', required=True, tracking=True)

    # Sinh viên quan hệ n-n với Ngành
    # 1 Ngành có nhiều Sinh viên, 1 Sinh viên có thể thuộc nhiều Ngành
    # Bảng phụ sẽ được tạo tự động với tên là student_faculty_rel
    # Sử dụng khóa ngoại để liên kết tới eaut.crm.faculty và eaut.crm.student
    student_ids = fields.Many2many(
        'eaut.crm.student',
        'student_major_rel',
        'major_id',
        'student_id',
        string='Students',
        tracking=True
    )

    # Ràng buộc Unique cho mã Ngành
    _sql_constraints = [
        ('major_code_unique', 'unique(code)', 'Major code must be unique!'),
    ]
