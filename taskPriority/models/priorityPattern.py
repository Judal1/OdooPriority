from odoo import models,fields;

class PriorityPattern(models.Model):
    _name = 'priority.pattern'

    name=fields.Char(string='Title',required=True)