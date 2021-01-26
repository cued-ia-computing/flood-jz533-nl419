from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""
    stations = build_station_list()
    cam_city_centre_coords = (52.2053, 0.1218)
    sorted_stations = [(i.name, i.town, d) for (i,d) in stations_by_distance(stations, cam_city_centre_coords)]
    print("Closest 10 stations: ")
    print(*sorted_stations[:10])
    print()
    print("Furthest 10 stations: ")
    print(*sorted_stations[-10:])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()