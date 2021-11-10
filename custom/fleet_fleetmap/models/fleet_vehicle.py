import logging
import pytraccar
import asyncio
import aiohttp
from pytraccar.api import API
from odoo import api, fields, models

HOST = "traccar.fleetmap.me"
PORT = 80
USERNAME = "admin"
PASSWORD = "admin"

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

        async with aiohttp.ClientSession() as session:
                data = API(LOOP, session, USERNAME, PASSWORD, HOST, PORT)
                await data.get_device_info()

                _logger.debug('LoginResult %s', data.device_info)

        return result
