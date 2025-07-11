from odoo import models, api

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        for rec in records:
            rec._sync_event_to_student()
        return records
    
    # def write(self, vals):
    #     res = super().write(vals)
    #     for rec in self:
    #         rec._sync_event_to_student()
    #     return res

    def _sync_event_to_student(self):
        for rec in self:
            # Nếu registration có email, tìm student tương ứng
            if rec.email and rec.event_id:
                student = self.env['eaut.crm.student'].search([('email', '=', rec.email)], limit=1)
                if student and rec.event_id.id not in student.event_ids.ids:
                    student.event_ids = [(4, rec.event_id.id)]  # (4, id) là thêm phần tử vào Many2many không ghi đè
