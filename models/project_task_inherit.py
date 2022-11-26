from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import datetime

class ProjectTask(models.Model):
    _inherit = "project.task"

    date_deadline = fields.Date(string='Deadline', index=True, copy=False, tracking=True)

    @api.onchange('date_deadline')
    def _onchange_date_deadline(self):
        new_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.date_deadline = new_date

    planned_hours = fields.Float("Initially Planned Hours",
                                 help='Time planned to achieve this task (including its sub-tasks).', tracking=True)
