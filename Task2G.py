from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import risk, riskDict
# from floodsystem.plot import plot_water_level_with_fit
# from floodsystem.geo import stations_by_river


def run():
    """Requirements for Task 2G"""
    stations = build_station_list()
    update_water_levels(stations)
    rel_level_threshold = 1.2
    high_stations = [i for i in stations if i.relative_water_level() is not None
                     and i.relative_water_level() > rel_level_threshold]
    print("Number of stations: {}".format(len(stations)))
    print("Number of high stations: {}".format(len(high_stations)))

    # debug code to check specific rivers' risk levels
    # river_dic = stations_by_river(stations)
    # for i in river_dic["River Hull"]:
    for i in high_stations:
        if i is None:
            continue
        if i.typical_range is None:
            continue
        print(i.name)
        print(riskDict[risk(i)])
        print()
        # Debug code for specific stations
        # if i.name in ["Clifford Bridge"]:
        #     dt = 6
        #     dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        #     plot_water_level_with_fit(i, dates, levels, 3, 1)


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
