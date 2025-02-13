from odoo import models,fields;

class PriorityPattern(models.Model):
    _name = 'priority.pattern'
    _order = 'name'

    title=fields.Char(string='Title',required=True)
    color=fields.Integer(string='Color', default=1)
