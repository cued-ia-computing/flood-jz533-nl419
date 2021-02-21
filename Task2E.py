from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels
from floodsystem.plot import plot_water_levels
import datetime


def run():
    """Requirements for Task 2E"""
    stations = build_station_list()
    update_water_levels(stations)
    list_of_top_5_stations = stations_highest_rel_level(stations, 5)

    for i in list_of_top_5_stations:
        dt = 10
        dates, levels = fetch_measure_levels(i.measure_id, dt=datetime.timedelta(days=dt))
        plot_water_levels(i, dates, levels)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
