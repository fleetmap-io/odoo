
from odoo import api, fields, models


class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    mobility_card_test = fields.Char(compute='_compute_mobility_card_test', store=True)

    def _compute_mobility_card_test(self):
        for vehicle in self:
            vehicle.mobility_card_test = '1'
