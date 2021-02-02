from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels


def run():
    """Requirements for Task 2B"""
    stations = build_station_list()
    update_water_levels(stations)
    total_list = stations_level_over_threshold(stations, 0.8)
    for i in total_list:
        list_of_objests = i[0]
        print(list_of_objests.name, i[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
