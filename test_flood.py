"""Unit test for the flood module"""

from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold


def test_stations_level_over_threshold():

    # Create stations
    s1 = MonitoringStation("s_id1", "m_id1", "A station", (1.0, 2.0), (1.0, 2.0), "r1", "t1")
    s2 = MonitoringStation("s_id2", "m_id2", "B station", (1.0, 4.0), (0.0, 2.0), "r2", "t2")
    s3 = MonitoringStation("s_id3", "m_id3", "C station", (1.0, 3.0), (3.0, 2.0), "r3", "t3")
    s4 = MonitoringStation("s_id4", "m_id4", "D station", (1.0, 5.0), (2.0, 3.0), "r4", "t4")
    s5 = MonitoringStation("s_id5", "m_id5", "E station", (1.0, 6.0), (4.0, 4.5), "r5", "t5")
    s1.latest_level = None
    s2.latest_level = 0.9
    s3.latest_level = 0.8
    s4.latest_level = 2.8
    s5.latest_level = 4.45
    stations = [s1, s2, s3, s4, s5]
    final_list_of_tuples = stations_level_over_threshold(stations, 0.5)

    assert final_list_of_tuples == [(s5, (4.45 - 4.0) / (4.5 - 4.0)), (s4, (2.8 - 2.0) / (3.0 - 2.0))]
