from datetime import date
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class CustomerDetails(models.Model):
    _name = "customer_details"
    _description = "Customer Details Model"
    name = fields.Char()
    description = fields.Text()
    address = fields.Text()
    city = fields.Text()
    state = fields.Text()
    country = fields.Text()
    pincode = fields.Integer()
    date_of_service = fields.Datetime(default=date.today())
    schedule = fields.Boolean()
    active = fields.Boolean(default=True)
    payment = fields.Boolean(default=False , compute="_compute_payment")
    progress = fields.Selection(string="Select the progress",
                                selection=[('new', 'New'), ('received', 'Service Received'), (
                                    'inprogress', 'In Progress'), ('done', 'Done'), ('cancelled', 'Cancelled')],
                                help="Select the progress")
    active = fields.Boolean('Active', default=True)
    service_id = fields.Many2one("service_type", string="service type")
    image = fields.Binary("image")
    service_provider_ids = fields.One2many(
        'employee_details', 'customer_id', required=True)
    age = fields.Integer(compute="_compute_age")
    date_of_birth = fields.Date()
    send_tip=fields.Integer()


    @api.depends('age', 'date_of_birth')
    def _compute_age(self):
        for record in self:
            if (record.date_of_birth):
                today = date.today()
                if record.date_of_birth.month < today.month and record.date_of_birth.day < today.day:
                    record.age = (today.year-record.date_of_birth.year)+1
                else:
                    record.age = today.year-record.date_of_birth.year
            else:
                record.age=0
    cost_service=fields.Integer()
    no_of_hours=fields.Integer()
    @api.depends('payment','progress','service_id.price_per_hour','cost_service','no_of_hours')
    def _compute_payment(self):
        for record in self:
            if(record.progress=='done'):
                record.payment=True
                record.cost_service=record.service_id.price_per_hour*record.no_of_hours
                
                
            else:
                record.payment=False
"""  @api.depends('send_tip','service_provider_ids.tip_recieved')
    def _compute_total_tip(self):
        for record in self:
            if(record.send_tip):
                record.service_provider_ids.tip_recieved=record.service_provider_ids.tip_recieved+record.send_tip
 """
               