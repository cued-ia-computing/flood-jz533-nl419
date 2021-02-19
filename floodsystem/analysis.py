import numpy as np
import matplotlib.dates


def polyfit(dates, levels, p):
    """Computes a least-squares fit of a polynomial of degree p to water level data,
    where dates = np.array of dates, and levels = np.array of the water level at each date.
    Returns (poly, d0) where poly is a np.poly1d object, and d0 is the date offset of the polynomial.
    """
    assert len(dates) == len(levels)
    numericalDates = matplotlib.dates.date2num(dates)

    # Note, sometimes the API returns a level of 2147484.0 m.
    # This may result in some unusual behaviour in the polynomial.
    p_coeff = np.polyfit(numericalDates - numericalDates[0], levels, p)
    poly = np.poly1d(p_coeff)
    return (poly, numericalDates[0])
