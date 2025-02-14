from odoo import models,fields;

class Importance(models.Model):
    _inherit = 'priority.pattern'
    _name = 'priority.importance'

    status = fields.Char(string='Status')
    sequence = fields.Integer(string='Sequence')

    _sql_constraints = [
        ('check_importance_name_unique', 'UNIQUE (name)', 'Importance title must be unique')
    ]
