# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine


def stations_by_distance(stations, p):
    """Sorts a list of stations by distance to a coordinate p

    Returns a list of (station, distance) tuples
    sorted in increasing order of distance,
    where distance (float) is the distance of the station
    (MonitoringStation) from the coordinate p
    """

    # Create list of tuples of (station, distance)
    station_distance = [(stations[i], haversine(stations[i].coord, p)) for i in range(len(stations))]
    return sorted_by_key(station_distance, 1)


def stations_within_radius(stations, centre, r):
    """Get list of stations within radius r of centre
    Returns a list of all stations (type MonitoringStation)
    within radius "r" of a geographic coordinate "centre"
    """

    return [i for i in stations if haversine(i.coord, centre) <= r]


def rivers_with_station(stations):
    """Get all rivers that have a station
    Returns set of rivers (string)
    """

    list_of_rivers = [i.river for i in stations]
    return set(list_of_rivers)


def stations_by_river(stations):
    """Map river names to a list of station objects on a given river
    Returns dictionary with format {river_name: [station1, station2, ...]}
    """

    river_dictionary = {}

    for i in stations:
        river_dictionary.setdefault(i.river, []).append(i)
    return river_dictionary


def rivers_by_station_number(stations, N):
    """Determine the N rivers with the greatest number of monitoring stations
    """
    river_dic = stations_by_river(stations)
    # Sort rivers by how many stations they have (in descending order)
    sorted_rivers = sorted_by_key([(river, len(station_list)) for (river, station_list) in river_dic.items()], 1, True)
    # Don't know how to make this more efficient, so here goes.
    sliced_rivers = sorted_rivers[:N]
    counter = N
    # While the last element of sliced_rivers has same number of stations as next item in sorted_rivers
    while sliced_rivers[-1][1] == sorted_rivers[counter][1]:
        sliced_rivers.append(sorted_rivers[counter])
        counter += 1
    return sliced_rivers
