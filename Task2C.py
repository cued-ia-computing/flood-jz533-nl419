from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.station import MonitoringStation


def run():
    """Requirements for Task 2C"""
    stations = build_station_list()
    update_water_levels(stations)
    total_sorted_list = stations_highest_rel_level(stations, 10)
    for i in total_sorted_list:
        print(i.name, MonitoringStation.relative_water_level(i))


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
