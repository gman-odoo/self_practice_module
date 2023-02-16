from odoo import models,fields
class ServiceType(models.Model):
    _name = "service_type"
    _description = "Services Type"
    name=fields.Char()
    price_per_hour=fields.Integer()