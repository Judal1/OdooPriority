from odoo import models,fields;

class Complexity(models.Model):
    _inherit = 'priority.pattern'
    _name = 'priority.complexity'

    color=fields.Integer(string='Color', default=1)

    _sql_constraints = [
        ('check_complexity_name_unique', 'UNIQUE (name)', 'Complexity title must be unique')
    ]
    _rec_name = 'color'