from odoo import api, fields, models, _


class Registration(models.Model):
    _name = 'school.registration'
    _description = 'registration'

    section_id = fields.Many2one('school.section','section')
    course_id = fields.Many2one('school.course','course')
    teacher_id = fields.Many2one('school.teacher','teacher')
    school_ids = fields.Many2many('school.student','registration_student_rel','registration_id','student_id','Student List')

