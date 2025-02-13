from odoo import models,fields;

class Complexity(models.Model):
    _inherit = 'priority.pattern'
    _name = 'priority.complexity'

    _sql_constraints = [
        ('check_complexity_title_unique', 'UNIQUE (title)', 'Complexity title must be unique')
    ]