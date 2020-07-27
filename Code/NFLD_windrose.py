import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from windrose import WindroseAxes, WindAxes, plot_windrose


def plotWindrose(filename, location, cmap, bin_interval=10, plt_type='bar', saveImage=False):
    """
    Plotting function to generate windrose (polar) diagrams for provided wind speed / directional data.
    Usage:
        'filename': type = str; location of .csv data file.
        'location': type = str; location where data was collected.
        'bins': type = np.array; np.arange(minspeed, maxspeed, bin_interval), e.g. np.array(0.001, 100, 10).
        'cmap': type = matplotlib.cm option; e.g. cmap=cm.hot.
        'plt_type': type = str; define plot type. 'bar', 'contour', 'contourf', 'box'.
        'saveImage': type = bool; do you want to save this image?

    """
    df = pd.read_csv(filename, header=1, low_memory=False)

    df.rename(columns={'Wind Dir (10s deg)': 'direction(10sdeg)',
                       'Wind Spd (km/h)': 'speed',
                       'Wind Dir Flag': 'direction_flag',
                       'Wind Spd Flag': 'speed_flag'}, inplace=True)
    df['direction'] = 10 * df['direction(10sdeg)']
    bins = np.arange(df['speed'].min(), df['speed'].max(), bin_interval)
    ax = WindroseAxes.from_ax()
    if plt_type == 'bar':
        ax.bar(df.direction.values, df.speed.values, bins=bins, cmap=cmap)
    if plt_type == 'contour':
        ax.contour(df.direction.values, df.speed.values, bins=bins, cmap=cmap)
    if plt_type == 'contourf':
        ax.contourf(df.direction.values, df.speed.values, bins=bins, cmap=cmap)
    if plt_type == 'box':
        ax.box(df.direction.values, df.speed.values, bins=bins, cmap=cmap)
    if location is not None:
        ax.set_title('Wind Polar Plot: {}'.format(location), fontsize=16)
    else:
        ax.set_title('Wind Polar Plot', fontsize=16)
    ax.set_legend(ncol=2, title='Wind Speed (km/h)')
    if saveImage:
        plt.savefig('C:/Users/Jacob/CMSC6950_py/Open_Science_Project/CMSC6950_FinalProject/Images/' + location + '.pdf')

    plt.show()
    return None


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


plotWindrose('C:/Users/Jacob/CMSC6950_py/Open_Science_Project/CMSC6950_FinalProject/Data/Gander_1980-2012.csv',
             location="Gander Airport",
             bin_interval=10,
             plt_type='contourf', cmap=cm.hot, saveImage=False)

plotMap(mapbounds=[[-59.5, 46, -52.5, 52]], lats=[47.6212, 47.3, 49.22, 48.95, 48.53],
        lons=[-52.7423, -54, -57.4, -54.58, -58.55], lat_0=47, lon_0=-53)
