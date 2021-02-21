from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    cam_city_centre_coords = (52.2053, 0.1218)
    nearby_stations = sorted([i.name for i in stations_within_radius(stations, cam_city_centre_coords, 10)])
    print(nearby_stations)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
