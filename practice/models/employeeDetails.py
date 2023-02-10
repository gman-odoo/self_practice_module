
from odoo import models,fields

class EmployeeDetails(models.Model):
    _name = "service_details"
    _description = "Service Details Model"
    name=fields.Char()
    description=fields.Text()
    job_position=fields.Text()
    phone_number=fields.Integer()
    email=fields.Char()
    languages=fields.Char()
    tags=fields.Char()
    payment_terms=fields.Text()
    bank=fields.Char()
    account_number =fields.Integer()
    geo_location=fields.Text()
    image=fields.Image()
    customer_id=fields.Integer()
    tip_recieved =fields.Integer()

     

    
