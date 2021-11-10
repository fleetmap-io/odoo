from odoo import api, fields, models

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    fleetmap_name = fields.Char('Name')
    fleetmap_id = fields.Integer('Fleetmap ID')


class FleetVehicleOdometer(models.Model):
    _inherit = 'fleet.vehicle.odometer'

    fleetmap_test = fields.Char('test')
    user_id = fields.Many2one('res.users', 'Responsible', default=lambda self: self.env.user, index=True)

    @api.model
    def create(self, vals):
        vals['fleetmap_test'] = 'teste'
        result = super(FleetVehicleOdometer, self).create(vals)


        return result

