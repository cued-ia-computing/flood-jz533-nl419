from floodsystem.station import MonitoringStation
from .utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
import matplotlib.dates as matdate


def stations_level_over_threshold(stations, tol):
    """A function that returns a list of tuples, where each tuple holds
    1.a ststion at which the latest relative water level is over tol and 2.
    the relative water level at the station. Returned list should be sorted."""
    list_of_stations = []
    for i in stations:
        if MonitoringStation.relative_water_level(i) is None:
            pass
        elif MonitoringStation.relative_water_level(i) > tol:
            one_tuple = (i, MonitoringStation.relative_water_level(i))
            list_of_stations.append(one_tuple)
        else:
            pass
    return sorted_by_key(list_of_stations, 1, True)


def stations_highest_rel_level(stations, N):
    """A function that returns a list of the N stations at which the
    relative water level is highest. List should be sorted in descending
    order."""
    list_of_stations_have_rel = []
    for i in stations:
        if MonitoringStation.relative_water_level(i) is None:
            pass
        else:
            one_tuple2 = (i, MonitoringStation.relative_water_level(i))
            list_of_stations_have_rel.append(one_tuple2)
    sorted_list = sorted_by_key(list_of_stations_have_rel, 1, True)
    final_total_list = []
    for i in sorted_list:
        final_total_list.append(i[0])
    return final_total_list[:N]


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
