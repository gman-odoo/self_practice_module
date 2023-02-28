
from odoo import models,fields,api

class EmployeeDetails(models.Model):
    _name = "employee_details"
    _description = "Employee Details Model"
    _inherits="{'customer_details','customer_id'}"
    name=fields.Char()
    description=fields.Text()
    job_position=fields.Char()
    phone_number=fields.Char()
    email=fields.Char()
    languages=fields.Char()
    payment_terms=fields.Text()
    bank=fields.Char()
    account_number =fields.Integer()
    geo_location=fields.Text()
    image=fields.Image()
    tip_recieved=fields.Integer(compute="_compute_total_tip",store=True)
    active=fields.Boolean('Active',default=True)
    state=fields.Selection(selection=[('work','Work In Progress'),('available','Available')])
    tag_ids=fields.Many2many('employee_tag',string="Tags")
    service_given_id=fields.Many2one('service_type',string="Service Provided")
    customer_id=fields.Many2one('customer_details')
    available_customer_id=fields.Many2one('customer_details')
    RATING=[
        ("0","No Rating"),
        ("1","one Rating"),
        ("2","Two Rating"),
        ("3","ThreeRating"),
        ("4","four rating"),
        ("5", "five rating")

    ]
    rating=fields.Selection(RATING,string="Rating",default="0")
    status=fields.Selection(selection=[('accept','Accept'),('refuse','Refuse')])
   

    @api.depends('tip_recieved','customer_id.send_tip')
    def _compute_total_tip(self):
        for record in self:
            record.tip_recieved=record.tip_recieved+record.customer_id.send_tip
    def action_accept(self):
        for record in self:
            record.status="accept"
            record.customer_id.state='received'
    def action_refused(self):
        for record in self:
            record.status="refuse"
            record.customer_id.state='cancelled'

    
               


     

    
