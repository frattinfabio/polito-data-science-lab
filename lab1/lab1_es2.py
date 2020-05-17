# LAB1 es.2

# 2.2.1
import json

from math import cos, acos, sin
def distance_coords(lat1, lng1, lat2, lng2):
    deg2rad = lambda x: x * 3.141592 / 180
    lat1, lng1, lat2, lng2 = map(deg2rad, [ lat1, lng1, lat2, lng2 ])
    R = 6378100 # Radius of the Earth, in meters
    return R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))

with open("to-bike") as f:
    obj = json.load(f)


stations = obj["network"]["stations"]
num_active_stations = len(list(filter(lambda x: x["extra"]["status"] == "online",stations)))
print("Active stations: " + str(num_active_stations))

# 2.2.2

bikes_available = sum(list(map(lambda x: x["free_bikes"], stations)))
free_docks = sum(list(map(lambda x: x["empty_slots"], stations)))
print("Bikes available: " + str(bikes_available))
print("Free docks: " + str(free_docks))

# 2.2.3

lat = 45.074512
long = 7.694419

min_dist = min(list(map(lambda x: distance_coords(x["latitude"], x["longitude"], lat, long), stations)))
closest_stations = list(filter(lambda x: distance_coords(x["latitude"], x["longitude"], lat, long) == min_dist, stations))

print("Closest station: " + closest_stations[0]["name"])
