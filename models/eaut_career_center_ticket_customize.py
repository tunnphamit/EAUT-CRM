# models/helpdesk_ticket.py
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    student_code = fields.Char(string="Student Code")

    @api.model_create_multi
    def create(self, vals_list):
        tickets = super().create(vals_list)
        Student = self.env['eaut.career.center.student'].sudo()

        for ticket, vals in zip(tickets, vals_list):
            email = vals.get('partner_email') or vals.get('email') or ticket.partner_email
            code_input = vals.get('student_code') or ticket.student_code
            if not email:
                continue

            # 1) Nếu email đã tồn tại → bỏ qua
            if Student.search([('email', '=', email)], limit=1):
                continue

            # 2) Nếu có nhập code và code đã tồn tại nhưng email khác → bỏ qua
            if code_input:
                existing_by_code = Student.search([('code', '=', code_input)], limit=1)
                if existing_by_code and existing_by_code.email != email:
                    continue  # bỏ qua, không tạo student

            # 3) Nếu không nhập code thì dùng sequence
            code_to_use = code_input or self.env['ir.sequence'].next_by_code('eaut.career.center.student')
            if not code_to_use:
                code_to_use = f"AUTO-{fields.Datetime.now():%Y%m%d%H%M%S}"

            # 4) Tạo student mới
            Student.create({
                'code': code_to_use,
                'name': vals.get('partner_name') or ticket.partner_name or ticket.name or email,
                'email': email,
                'phone': vals.get('phone') or '',
            })

        return tickets
