from odoo import models,fields;

class Task(models.Model):
    _inherit = 'project.task'

    importance_id = fields.Many2one('priority.importance', string='Importance')
    complexity_id = fields.Many2one('priority.complexity', string='Complexity')



