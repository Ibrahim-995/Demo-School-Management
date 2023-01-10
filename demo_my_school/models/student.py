
from odoo import api, fields, models, _


class Student(models.Model):
    _name = "school.student"
    _description = 'student'

    image = fields.Image(string="Profile Picture")
    name = fields.Char('Student Name', required=True)
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of birth')
    gender = fields.Selection([('M','Male'),('F','Female')],'Gender')



