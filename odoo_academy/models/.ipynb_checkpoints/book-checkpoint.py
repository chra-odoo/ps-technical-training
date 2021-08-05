# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Book(models.Model):

    _name = 'academy.book'
    _description = 'Book'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    isbn = fields.Char(string='ISBN')
    authors = fields.Char(string='Authors')
    year_of_edition = fields.Char(string='Year of Edition')
    genre = fields.Char(string='Genre')
    editors = fields.Char(string='Editors')
    note = fields.Text(string='Text')
    rental_id = fields.Many2one(comodel_name='rental.rental', string='Rental')
    
    @api.onchange('isbn')
    def _onchange_isbn(self):
        if self.isbn and len(self.isbn) != 13:
            raise ValidationError('The ISBN needs to be 13 characters long: %s' % self.isbn)