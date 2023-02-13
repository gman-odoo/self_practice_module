from datetime import datetime
from odoo import models,fields

class CustomerDetails(models.Model):
    _name = "customer_details"
    _description = "Customer Details Model"
    name=fields.Char()
    description=fields.Text()
    address=fields.Text()
    city=fields.Text()
    state=fields.Text()
    country=fields.Text()
    pincode=fields.Integer()
    date_of_service=fields.Datetime(default=datetime.now())
    schedule=fields.Boolean()
    active=fields.Boolean()
    payment=fields.Boolean(default=False)
    progress=fields.Selection(string="Select the progress",
    selection=[('new','New'),('received','Service Received'),('inprogress','In Progress'),('done','Done'),('cancelled','Cancelled')],
    help="Select the progress")
    active=fields.Boolean('Active',default=True)
    service_id=fields.Many2one("service_type", string="service type")
    image=fields.Binary("image")

