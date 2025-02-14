from odoo import models,fields,api;


class Task(models.Model):
    _inherit = 'project.task'

    importance_id = fields.Many2one('priority.importance', string='Importance')
    complexity_id = fields.Many2one('priority.complexity', string='Complexity')
    complexity_color = fields.Char(string='Complexity Color', compute='_compute_complexity_color')
    importance_sequence = fields.Integer(string='Importance Sequence', compute='_compute_importance_sequence', store=True)


    @api.depends('complexity_id')
    def _compute_complexity_color(self):
        for r in self:
            r.complexity_color = r.complexity_id.color;

    @api.depends('importance_id')
    def _compute_importance_sequence(self):
        for r in self:
            if(r.importance_id):
                r.importance_sequence = r.importance_id.sequence;
            else:
                r.importance_sequence = 2147483647;

