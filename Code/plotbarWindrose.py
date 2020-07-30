import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.basemap import Basemap
from windrose import WindroseAxes, WindAxes, plot_windrose

def plotbarWindrose(filename, location, cmap=cm.hot, bin_interval=10):
    """
    Plotting function to generate windrose bar diagram for provided wind speed / directional data.
    Usage:
        'filename': type = str; location of .csv data file.
        'location': type = str; location where data was collected.
        'bins': type = np.array; np.arange(minspeed, maxspeed, bin_interval), e.g. np.array(0.001, 100, 10).
        'cmap': type = matplotlib.cm option; e.g. cmap=cm.hot.
    """
    df = pd.read_csv(filename, header=1, low_memory=False)

    df.rename(columns={'Wind Dir (10s deg)': 'direction(10sdeg)',
                       'Wind Spd (km/h)': 'speed',
                       'Wind Dir Flag': 'direction_flag',
                       'Wind Spd Flag': 'speed_flag'}, inplace=True)
    df['direction'] = 10 * df['direction(10sdeg)']
    bins = np.arange(df['speed'].min(), df['speed'].max(), bin_interval)
    ax = WindroseAxes.from_ax()
    ax.bar(df.direction.values, df.speed.values, bins=bins, cmap=cmap)
    ax.set_title('Wind Polar Plot: {}'.format(location), fontsize=16)
    ax.set_legend(ncol=2, title='Wind Speed (km/h)')

    plt.savefig('C:/Users/Jacob/CMSC6950_py/Open_Science_Project/CMSC6950_FinalProject/bar.pdf')

    plt.show()
    return None


def main(args):
    if len(args) != 3:
        raise SystemExit('Stopped')

    plotbarWindrose(filename=args[1], location=args[2])


if __name__ == '__main__':
    import sys

    main(sys.argv)