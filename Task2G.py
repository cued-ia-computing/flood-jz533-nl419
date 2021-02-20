from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import polyfit
import datetime
import matplotlib.dates as matdate
# from floodsystem.plot import plot_water_level_with_fit
# from floodsystem.geo import stations_by_river


riskDict = {0: "Low", 1: "Moderate", 2: "High", 3: "Severe"}


def risk(station):
    """Returns the risk level of flooding at the given station,
    0 = low, 1 = moderate, 2 = high, 3 = severe"""

    # See if water level is rising or falling, using last 3 days' data
    # Note: polyfit is incredibly bad at predicting future water levels.
    # However, it is useful for seeing if the water level is rising or falling currently.
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=3))
    poly, d0 = polyfit(dates, levels, 3)
    total = 0
    rate = poly.deriv()
    # Oddly, the first item in dates[] is the latest date.
    # I.e. it is in reverse chronological order.
    currentRate = rate(matdate.date2num(dates[0]) - d0)

    # Add score based on current rate of water level change
    total += currentRate * 2

    # Also add on score for current river level
    total += station.relative_water_level()
    # Return number according to score
    # These thresholds were determined by looking at typical distribution of stations with certain scores,
    # and by looking at gov.uk flood warnings at the time of writing this code (20/02/2021)

    if total > 20:
        return 3
    if total > 10:
        return 2
    if total > 4:
        return 1
    return 0

    # Debug code - return score instead of risk level
    # return total


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
