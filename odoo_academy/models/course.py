# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    
    _name = 'academy.course'
    _description = 'Course Info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level = fields.Selection(string='Level', selection=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')])
    isbn = fields.Char(string='ISBN')
    authors = fields.Char(string='Authors')
    year_of_edition = fields.Char(string='Year of Edition')
    genre = fields.Char(string='Genre')
    editors = fields.Char(string='Editors')
    active = fields.Boolean(string="Active")