import pytz
from flask_restplus import Namespace, Resource, fields
from datetime import datetime
from dateutil import zoneinfo

api = Namespace('time', description='a set of API for time.')

zone = api.model('Zone', {
    'name': fields.String(required=True, description='zone name')
})

current_time = api.model('ZoneTime', {
    'name': fields.String(required=True, description='zone name'),
    'time': fields.String(required=True, description='zone time')
})

ZONE_LIST = [{'name': zone} for zone in zoneinfo.get_zonefile_instance().zones.keys()]


@api.route('/')
class ListZone(Resource):
    @api.doc('list_zone')
    @api.marshal_list_with(zone)
    def get(self):
        """List all available zone name."""
        return ZONE_LIST


@api.route('/<name>')
@api.param('name', 'zone name')
@api.response(404, "It's not an available zone name.")
class ZoneTime(Resource):
    @api.doc('get_zone_time')
    @api.marshal_with(current_time)
    def get(self, name):
        """Fetch a zone time."""
        zone_time = datetime.now().astimezone(pytz.timezone(name))
        return {'name': name, 'time': zone_time}
        api.abort(404)
