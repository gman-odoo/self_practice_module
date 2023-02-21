from odoo import models,fields
class ServiceType(models.Model):
    _name = "service_type"
    _description = "Services Type"
    name=fields.Char()
    price_per_hour=fields.Integer()
    emp_ids=fields.One2many('employee_details','service_id',string="Assigned Service Providers")