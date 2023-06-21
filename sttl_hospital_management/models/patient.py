from odoo import fields, api, models


class HospitalPatient(models.Model):
    _name='res.hospital' # named as res_hospital in database(hospital_db)
    _description='Hospital patient Registration data'

    name=fields.Char(string='Name')
    dob=fields.Date(string='Date of Birth')
    contact=fields.Char(string='Contact',size=10)
    gender=fields.Selection([('male', 'Male'),('female','Female'),('other','Other')],string='Gender')
