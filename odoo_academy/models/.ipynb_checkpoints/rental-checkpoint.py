# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rental(models.Model):
    _name = 'rental.rental'
    _description = 'Book Rental'
    
    customer_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    book_ids = fields.One2many(comodel_name='academy.book.copy', inverse_name='rental_id', string='Books')