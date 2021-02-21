from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river


def run():
    """Requirements for Task 1D"""
    stations = build_station_list()

    # Demonstrate rivers_with_station()
    print("Number of rivers with station:")
    print(len(rivers_with_station(stations)))
    print("First 10 rivers: ")
    print(sorted(rivers_with_station(stations))[:10])

    # Demonstrate stations_by_river
    river_dic = stations_by_river(stations)
    print("Stations located on rivers: ")
    print("River Aire: ", end="")
    print(sorted([i.name for i in river_dic["River Aire"]]))
    print("River Cam: ", end="")
    print(sorted([i.name for i in river_dic["River Cam"]]))
    print("River Thames: ", end="")
    print(sorted([i.name for i in river_dic["River Thames"]]))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
