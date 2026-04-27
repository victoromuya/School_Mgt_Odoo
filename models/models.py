# -*- coding: utf-8 -*-

from odoo import models, fields


class StudentRecord(models.Model):
    _name = 'student.record'
    _description = 'Student Record'

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    active = fields.Boolean(string='Active', default=True)

    def deactivate_student(self):
        for record in self:
            record.write({'active': False})