
from odoo import models, fields


class EautCareerCenterStudentRegistration(models.Model):
    _name = 'eaut.career.center.student.registration'
    _description = 'Student Registration'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Title', required=True, tracking=True)
    student_id = fields.Many2one('eaut.career.center.student', string='Student', required=True, tracking=True)
    deadline = fields.Date(string='Deadline', tracking=True)
    assign_to = fields.Many2one('res.users', string='Assign To', tracking=True)
    description = fields.Text(string="Description")

    # Quan hệ với Stage
    stage_id = fields.Many2one(
        'eaut.career.center.stage',
        string="Stage",
        tracking=True,
        index=True,
        group_expand='_read_group_stage_ids',
        domain="[('model_type', '=', 'student_registration')]"
    )