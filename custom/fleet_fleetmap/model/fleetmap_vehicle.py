class FleetVehicle(models.Model):
    _name = 'fleet.vehicle'
    _inherit = ['fleet.vehicle']

    fleetmap_name = fields.Char('Name')
    fleetmap_id = fields.Integer('Fleetmap ID')
