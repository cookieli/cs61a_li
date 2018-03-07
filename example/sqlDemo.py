from collections import namedtuple
CitiesRow = namedtuple("Row", ["latitude", "longitude", "name"])
cities = [CitiesRow(38, 122, "Berkeley"),
          CitiesRow(42,  71,  "Cambridge"),
          CitiesRow(43,  93,  "Minneapolis")]
DistancesRow = namedtuple("Row", ["name", "distance"])
def select(cities_row):
    latitude, longitude, name = cities_row
    return DistancesRow(name, 60*abs(latitude-38))
