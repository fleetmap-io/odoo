from odoo import fields, models

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    fleetmap_name = fields.Char('Name')
    fleetmap_id = fields.Integer('Fleetmap ID')


