import pytz
from flask_restplus import Namespace, Resource, fields
from datetime import datetime
from dateutil import zoneinfo

time_api = Namespace('time', description='a set of API for time.')

zone = time_api.model('Zone', {
    'name': fields.String(required=True, description='zone name')
})

current_time = time_api.model('ZoneTime', {
    'name': fields.String(required=True, description='zone name'),
    'time': fields.String(required=True, description='zone time')
})

ZONE_LIST = [{'name': zone} for zone in zoneinfo.get_zonefile_instance().zones.keys()]


@time_api.route('/')
class ListZone(Resource):
    @time_api.doc('list_zone')
    @time_api.marshal_list_with(zone)
    def get(self):
        """List all available zone name."""
        return ZONE_LIST


@time_api.route('/<name>')
@time_api.param('name', 'zone name')
@time_api.response(404, "It's not an available zone name.")
class ZoneTime(Resource):
    @time_api.doc('get_zone_time')
    @time_api.marshal_with(current_time)
    def get(self, name):
        """Fetch a zone time."""
        zone_time = datetime.now().astimezone(pytz.timezone(name))
        return {'name': name, 'time': zone_time}
