import logging
from pytraccar.exceptions import (
    ForbiddenAccessException,
    InvalidTokenException,
    BadRequestException,
    ObjectNotFoundException,
    UserPermissionException
)
from pytraccar import api as traccar
from odoo import api, fields, models

username, password = 'admin', 'admin'
traccar_url = 'https://traccar.fleetmap.me/'
_logger = logging.getLogger('fleetmap')

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

        user = traccar.TraccarAPI(base_url=traccar_url)
        loginResult = user.login_with_credentials(username, password)

        _logger.debug('LoginResult %s', loginResult)

        return result
