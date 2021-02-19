import matplotlib.dates
import matplotlib.pyplot as plt
from .analysis import polyfit


def plot_water_levels(station, dates, levels):
    """A function that displays a plot of the water level data against time
    for a station, and include on the plot lines for the typical low and
    high levels"""
    name_of_station = station.name
    typical_low = station.typical_range[0]
    typical_high = station.typical_range[1]

    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(name_of_station)
    plt.xticks(rotation=45)
    plt.axhline(y=typical_low)
    plt.axhline(y=typical_high)

    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    numericalDates = matplotlib.dates.date2num(dates)

    plt.plot(dates, poly(numericalDates - d0))
    plt.plot(dates, levels)
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.title(station.name)
    plt.xticks(rotation=45)
    plt.axhline(y=station.typical_range[0])
    plt.axhline(y=station.typical_range[1])

    plt.tight_layout()
    plt.show()
