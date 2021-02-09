"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from haversine import haversine


def test_stations_by_distance():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (0.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 2.0), (0.0, 2.0), "r2", "t2")
    stations = [s1, s2]
    list_of_tuples = stations_by_distance(stations, (2.0, 2.0))

    assert list_of_tuples == [(s2, haversine((1.0, 2.0), (2.0, 2.0))), (s1, haversine((0.0, 2.0), (2.0, 2.0)))]
