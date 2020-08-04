import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
import sys


def plotMap(loc):
    """

    """

    places = ['Argentia_1953-1970',
              'Buchans_1953-1965',
              'Cartwright_2015-2018',
              'ChurchillFalls_2011-2019',
              'DeerLake_1980-2012',
              'Gander_1980-2012',
              'GooseBay_1990-2019',
              'Makkovik_2015-2019',
              "Mary'sHarbour_2013-2015",
              'Nain_1990-2015',
              'Saglek_1991-1994',
              'St.Anthony_2009-2012',
              'St.Johns_2012-2019',
              'Stephenville_1980-2012',
              'WabushLake_1985-2013']

    lat_lons = [(47.3, -54),
                (48.85, -56.83),
                (53.68, -57.04),
                (53.56, -64.11),
                (49.22, -57.4),
                (48.95, -54.58),
                (53.32, -60.42),
                (55.08, -59.19),
                (52.3, -55.85),
                (56.55, -61.68),
                (58.47, -62.65),
                (51.39, -56.07),
                (47.62, -52.74),
                (48.53, -58.55),
                (52.93, -66.87)]

    locations = dict(zip(places, lat_lons))

    plt.figure(figsize=(20, 20))
    mapbounds = [[-63, 46, -52.5, 60]]
    map = [Basemap(i, j, k, l, resolution='i', projection='tmerc', lat_0=47, lon_0=-53) for i, j, k, l in mapbounds]
    m = map[0]
    coords = m(locations[loc][1], locations[loc][0])

    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral', lake_color='aqua')
    m.drawcoastlines()
    m.plot(coords[0], coords[1], marker='o', color='red', markersize=10)
    plt.savefig('location.pdf')
    plt.show()


def main(args):
    if len(args) != 2:
        raise SystemExit('Stopped')
    plotMap(loc=args[1])


if __name__ == '__main__':
    main(sys.argv)
