from odoo import fields, models

class EautCrmProgram(models.Model):
    _name = 'eaut.career.center.program'
    _description = 'Program' # Khóa
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # Tên Khóa (ví dụ: K11)
    name = fields.Char(string='Program name', required=True, tracking=True)
    
    # Năm khởi tạo
    start_year = fields.Char(string='Start year', tracking=True)

    # Quan hệ N:N: 1 chương trình nhiều sinh viên, 1 sinh viên nhiều chương trình
    student_ids = fields.Many2many(
        'eaut.career.center.student',
        'student_program_rel',
        'program_id',
        'student_id',
        string='Students',
        tracking=True
    )

    # Ràng buộc Unique cho mã Khóa
    # _sql_constraints = [
    #     ('program_code_unique', 'unique(code)', 'Program code must be unique!'),
    # ]
