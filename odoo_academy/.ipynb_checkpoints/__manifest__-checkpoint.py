# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage training""",
    'description': """
    Academy Module to manage training:
    - courses
    - sessions
    - attendees    
    """,
    'author': 'Odoo',
    'website': 'https://www.odoo.com',
    'category': 'Training',
    'version': '1.0',
    'depends': ['web_map', 'sale', 'website'],
    'data': [
                'security/academy_security.xml',
                'security/books_security.xml',
                'security/ir.model.access.csv',
                'views/academy_menuitems.xml',
                'views/books_menuitems.xml',
                'views/rental_menuitems.xml',
                'views/course_views.xml',
                'views/book_views.xml',
                'views/session_views.xml',
                'views/rental_views.xml',
                'views/sale_views_inherit.xml',
                'views/product_views_inherit.xml',
                'wizard/sale_wizard_view.xml',
                'report/session_report_templates.xml',
                'views/academy_web_templates.xml'
            ],
    'demo': [
            ],
}