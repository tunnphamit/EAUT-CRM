from odoo import fields, models

class Faculty(models.Model):
    _name = 'eaut.crm.faculty'
    _description = 'Faculty' # Khoa
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Mã Khoa
    code = fields.Char(string='Faculty code', required=True, tracking=True)

    # Tên Khoa
    name = fields.Char(string='Faculty name', required=True, tracking=True)

    # Sinh viên quan hệ n-n với Khoa
    # 1 Khoa có nhiều Sinh viên, 1 Sinh viên có thể thuộc nhiều Khoa
    # Bảng phụ sẽ được tạo tự động với tên là student_faculty_rel
    # Sử dụng khóa ngoại để liên kết tới eaut.crm.faculty và eaut.crm.student
    student_ids = fields.Many2many(
        'eaut.crm.student',
        'student_faculty_rel', # Tên bảng phụ để liên kết n-n
        'faculty_id',  # Khóa ngoại liên kết tới eaut.crm.faculty
        'student_id', # Khóa ngoại liên kết tới eaut.crm.student
        string='Students',
        tracking=True
    )

    # Ràng buộc Unique cho mã khoa
    _sql_constraints = [
        ('faculty_code_unique', 'unique(code)', 'Faculty code must be unique!'),
    ]
