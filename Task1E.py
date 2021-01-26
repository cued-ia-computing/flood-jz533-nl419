from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    """Requirements for Task 1C"""
    stations = build_station_list()
    print("Top 9 rivers by station number (including ties for 9th place): ")
    print(rivers_by_station_number(stations, 9))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
