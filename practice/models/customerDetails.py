from datetime import datetime
from odoo import models,fields

class CustomerDetails(models.Model):
    _name = "customer_details"
    _description = "Customer Details Model"
    name=fields.Char()
    description=fields.Char()
    address=fields.Text()
    city=fields.Text()
    state=fields.Text()
    country=fields.Text()
    pincode=fields.Integer()
    date_of_service=fields.Datetime(default=datetime.now())
    schedule=fields.Boolean()
    active=fields.Boolean()
    payment=fields.Boolean(default=False)
    service=fields.Selection(string="Service",
    selection=[('cleaning','Cleaning'),('mechanic','Mechanic'),('repairs','Repairs'),('salon','Salon')],
    help="Select the type of service")
    progress=fields.Selection(string="Select the progress",
    selection=[('new','New'),('received','Service Received'),('inprogress','In Progress'),('done','Done'),('cancelled','Cancelled')],
    help="Select the progress")
    active=fields.Boolean('Active',default=True)

