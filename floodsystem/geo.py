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
    station_distance = [(stations[i], haversine(stations[i].coord,p)) for i in range(len(stations))]
    return sorted_by_key(station_distance, 1)

def stations_within_radius(stations, centre, r):
    """Get list of stations within radius r of centre
    returns a list of all stations (type MonitoringStation) 
    within radius "r" of a geographic coordinate "centre"
    """

    return [i for i in stations if haversine(i.coord, centre) <= r]