import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from windrose import WindroseAxes, WindAxes, plot_windrose


def plotMap(mapbounds, lats, lons, lat_0, lon_0):
    """

    """
    cords = []
    plt.figure(figsize=(10, 10))
    map = [Basemap(i, j, k, l, resolution='i', projection='tmerc', lat_0=lat_0, lon_0=lon_0)
           for i, j, k, l in mapbounds]
    m = map[0]
    [cords.append(m(i, j)) for i, j in zip(lons, lats)]

    m.drawmapboundary(fill_color='aqua')
    m.fillcontinents(color='coral', lake_color='aqua')
    m.drawcoastlines()
    [m.plot(x, y, marker='o', color='red', markersize=10) for x, y in cords]

    plt.show()