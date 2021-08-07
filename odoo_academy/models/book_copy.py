# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookCopy(models.Model):
    
    _name = 'academy.book.copy'
    _inherits = {
        'academy.book': 'book_id'
    }
    _sql_constraints = [('sql_constraint_internal_ref', 'UNIQUE (internal_ref)', 'The Internal Reference must be unique.')]
    
    internal_ref = fields.Char(string='Internal Reference')
    book_id = fields.Many2one(comodel_name="academy.book", string="Book", required=True, ondelete="cascade")
    rental_id = fields.Many2one(comodel_name="rental.rental", string="Rental")