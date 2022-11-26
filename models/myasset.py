from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import datetime
import pytz


class MyAsset(models.Model):
    _name = 'my.asset'
    _description = 'My Asset'

    asset_no = fields.Char(string='Asset No', readonly=True, compute='_compute_asset_no')
    description = fields.Text(string="Description")
    location = fields.Char(string='Location')
    date = fields.Date(string='Date')
    Price = fields.Integer(
        string='Price',
        default=True)
    owner = fields.Many2one(comodel_name='res.partner', string='Owner', auto_join=True, tracking=True)

    def _compute_asset_no(self):
        for partner in self:
            partner.asset_no = datetime.datetime.now(pytz.timezone(partner.asset_no or 'GMT')).strftime('%Y%m%d%H%M')

    @api.onchange('owner')
    def _onchange_owner(self):
        new_date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.date = new_date
