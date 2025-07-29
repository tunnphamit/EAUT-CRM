

from odoo import fields, models

class EautCareerCenterTag(models.Model):
    _name = 'eaut.career.center.employer.industry'
    _description = 'Employer industry'

    name = fields.Char(string='Industry name', required=True)
    description = fields.Text(string="Description")