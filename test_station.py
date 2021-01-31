# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range_stations():

    # Create three stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (1, 2), (-2, 3), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (3, 4), None, "r2", "t2")
    s3 = MonitoringStation("s_id3", "m_id3", "C station", (5, 6), (3, -2), "r3", "t3")
    stations = [s1, s2, s3]
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    assert inconsistent_stations == ["B station", "C station"]
