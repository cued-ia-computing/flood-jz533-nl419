from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import risk, riskDict


def run():
    """Requirements for Task 2G"""
    stations = build_station_list()
    update_water_levels(stations)
    rel_level_threshold = 1.2
    high_stations = [i for i in stations if i.relative_water_level() is not None
                     and i.relative_water_level() > rel_level_threshold]
    print("Number of stations: {}".format(len(stations)))
    print("Number of high stations: {}".format(len(high_stations)))
    print("Determining risk levels. Please wait.")
    print("Depending on internet speed and cache availability, this may take up to 30 seconds...")

    town_risk_level = [(riskDict[risk(station)], station.town) for station in high_stations
                       if station.typical_range is not None and station.town is not None]

    town_risk_dict = {"Low": [], "Moderate": [], "High": [], "Severe": []}
    for tup in town_risk_level:
        town_risk_dict[tup[0]].append(tup[1])

    print("If the town is not included in any of the following lists, it either")
    print("\t1) does not have a nearby monitoring station with a valid output, or")
    print("\t2) is at low risk of flooding.\n")
    print("Low risk: \n{}.\n".format(", ".join(town_risk_dict["Low"])))
    print("Moderate risk: \n{}.\n".format(", ".join(town_risk_dict["Moderate"])))
    print("High risk: \n{}.\n".format(", ".join(town_risk_dict["High"])))
    print("Severe risk: \n{}.\n".format(", ".join(town_risk_dict["Severe"])))
    print("End of risk levels.")


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
