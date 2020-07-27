import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from windrose import WindroseAxes, WindAxes, plot_windrose


def plot(filename, location, bins, cmap, plt_type='bar'):
    """
    Plotting function to generate windrose (polar) diagrams for provided wind speed / directional data.
    Usage:
        'filename': type = str; location of .csv data file.
        'location': type = str; location where data was collected.
        'bins': type = np.array; np.arrange(minspeed, maxspeed, bin_interval), e.g. np.array(0.001, 100, 10).
        'cmap': type = matplotlib.cm option; e.g. cmap=cm.hot.
        'plt_type': type = str; define plot type. 'bar', 'contour', 'contourf', 'box'.

    """
    df = pd.read_csv(filename, header=1, dtype={'Year': int, 'Month': int, 'Day': int, 'Time': str,
                                                'Wind Dir (10s deg)': float, 'Wind dir Flag': str,
                                                'Wind Spd (km/h)': float, 'Wind Spd Flag': str}, low_memory=False)

    df.rename(columns={'Wind Dir (10s deg)': 'direction(10sdeg)',
                       'Wind Spd (km/h)': 'speed',
                       'Wind Dir Flag': 'direction_flag',
                       'Wind Spd Flag': 'speed_flag'}, inplace=True)
    df['direction'] = 10 * df['direction(10sdeg)']

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
    plt.show()
    return None


plot('C:/Users/Jacob/CMSC6950_py/Open_Science_Project/CMSC6950_FinalProject/Data/st_johns_intl_a_2012_2019.csv',
     location="St. John's Airport",
     bins=np.arange(0.01, 100, 10),
     plt_type='contourf', cmap=cm.hot)
