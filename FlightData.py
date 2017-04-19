print "Flight Data"

from opensky_api import OpenSkyApi
import json

api = OpenSkyApi()
s = api.get_states()
print(s)

