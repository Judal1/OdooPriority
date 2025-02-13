from odoo import models,fields;

class Importance(models.Model):
    _inherit = 'priority.pattern'
    _name = 'priority.importance'

    _sql_constraints = [
        ('check_importance_title_unique', 'UNIQUE (title)', 'Importance title must be unique')
    ]