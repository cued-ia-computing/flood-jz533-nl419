from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime


def run():
    """Requirements for Task 2F"""
    stations = build_station_list()
    update_water_levels(stations)
    list_of_top_5_stations = stations_highest_rel_level(stations, 5)

    for i in list_of_top_5_stations:
        dt = 2
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_level_with_fit(i, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
