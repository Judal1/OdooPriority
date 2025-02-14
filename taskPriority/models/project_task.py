from odoo import models,fields,api;

class Task(models.Model):
    _inherit = 'project.task'

    importance_id = fields.Many2one('priority.importance', string='Importance')
    complexity_id = fields.Many2one('priority.complexity', string='Complexity')
    complexity_color = fields.Char(string='Complexity Color', compute='_compute_complexity_color')


    @api.depends('importance_id')
    def _compute_complexity_color(self):
        for r in self:
            r.complexity_color = r.complexity_id.color;

