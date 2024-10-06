from math import radians,cos,sin,asin,sqrt
from itertools import permutations

EARTH_RADIUS = 3959
OFFICE = {"lat": 51.49984, "long": -0.124663}

from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
      dLat=radians(lat2-lat1)
      dLon=radians(lon2-lon1)
      lat1=radians(lat1)
      lat2=radians(lat2)
      a=sin(dLat/2)**2+cos(lat1)*cos(lat2)*sin(dLon/2)**2
      c=2*asin(sqrt(a))
      return EARTH_RADIUS*c

def sum_dist(a):
    return sum(haversine(*a[i],*a[i+1]) for i in range(len(a)-1))

def travel_expenses(a):
    if not all(-90<=i['lat']<=90 and -180<=i['long']<=180 for i in a):
        return "I am claiming extra holiday!"
    o,m=[(OFFICE['lat'],OFFICE['long'])],1e9
    for i in permutations([(i['lat'],i['long']) for i in a]):
        m=min(m,sum_dist(o+list(i)+o))
    return 500+m*10

print(travel_expenses([
  {"lat": 55.8642, "long": -4.2518},
  {"lat": 52.4862, "long": -1.8904},
  {"lat": 53.2268, "long": -0.5379},
  {"lat": 53.5229, "long": -1.1312}
]))