from floodsystem.stationdata import update_water_levels
from floodsystem.station import MonitoringStation
from .utils import sorted_by_key


def stations_level_over_threshold(stations, tol):
    """A function that returns a list of tuples, where each tuple holds
    1.a ststion at which the latest relative water level is over tol and 2.
    the relative water level at the station. Returned list should be sorted."""
    list_of_stations = []
    update_water_levels(stations)
    for i in stations:
        if MonitoringStation.relative_water_level(i) is None:
            pass
        elif MonitoringStation.relative_water_level(i) > tol:
            one_tuple = (i, MonitoringStation.relative_water_level(i))
            list_of_stations.append(one_tuple)
        else:
            pass
    return sorted_by_key(list_of_stations, 1, True)
