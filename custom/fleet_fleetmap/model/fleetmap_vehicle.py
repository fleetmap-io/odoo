from odoo import fields, models, _

class FleetVehicle(models.Model):
    _inherit = ['fleet.vehicle']

    fleetmap_name = fields.Char('Name')
    fleetmap_id = fields.Integer('Fleetmap ID')
