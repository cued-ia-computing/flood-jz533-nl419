"""Unit test for the geo module"""

from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_by_station_number


def test_stations_by_distance():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (0.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 2.0), (0.0, 2.0), "r2", "t2")
    stations = [s1, s2]
    list_of_tuples = stations_by_distance(stations, (2.0, 2.0))

    assert list_of_tuples == [(s2, haversine((1.0, 2.0), (2.0, 2.0))), (s1, haversine((0.0, 2.0), (2.0, 2.0)))]


def test_stations_within_radius():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (1.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 4.0), (0.0, 2.0), "r2", "t2")
    s3 = MonitoringStation("s_id3", "m_id3", "C station", (1.0, 3.0), (3.0, 2.0), "r3", "t3")
    stations = [s1, s2, s3]

    assert stations_within_radius(stations, (1.0, 1.0), 300) == [s1, s3]


def test_rivers_with_station():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (1.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 4.0), (0.0, 2.0), "r2", "t2")
    s3 = MonitoringStation("s_id3", "m_id3", "C station", (1.0, 3.0), (3.0, 2.0), "r2", "t3")
    stations = [s1, s2, s3]

    assert rivers_with_station(stations) == {'r2', 'r1'}


def test_stations_by_river():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (1.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 4.0), (0.0, 2.0), "r2", "t2")
    s3 = MonitoringStation("s_id3", "m_id3", "C station", (1.0, 3.0), (3.0, 2.0), "r3", "t3")
    stations = [s1, s2, s3]

    assert stations_by_river(stations) == {'r1': [s1], 'r2': [s2], 'r3': [s3]}


def test_rivers_by_station_number():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (1.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 4.0), (0.0, 2.0), "r2", "t2")
    s3 = MonitoringStation("s_id3", "m_id3", "C station", (1.0, 3.0), (3.0, 2.0), "r2", "t3")
    s4 = MonitoringStation("s_id4", "m_id4", "D station", (1.0, 2.0), (1.0, 2.0), "r3", "t4")
    s5 = MonitoringStation("s_id5", "m_id5", "E station", (1.0, 4.0), (0.0, 2.0), "r3", "t5")
    s6 = MonitoringStation("s_id6", "m_id6", "F station", (1.0, 3.0), (3.0, 2.0), "r3", "t6")
    stations = [s1, s2, s3, s4, s5, s6]
    assert rivers_by_station_number(stations, 2) == [('r3', 3), ('r2', 2)]
