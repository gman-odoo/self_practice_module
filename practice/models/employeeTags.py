from odoo import models,fields
class EmployeeTag(models.Model):
    _name = "employee_tag"
    _description = "Employee Tag"
    name=fields.Char()
    color=fields.Integer()