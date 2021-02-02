from floodsystem.station import MonitoringStation
from .utils import sorted_by_key


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
