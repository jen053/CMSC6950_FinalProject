import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from windrose import WindroseAxes, WindAxes, plot_windrose


def plot(filename, bins, cmap, plt_type='bar'):
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
    ax.set_legend(ncol=2)
    plt.show()
    return None


plot('C:/Users/Jacob/CMSC6950_py/Open_Science_Project/CMSC6950_FinalProject/Data/st_johns_a_2000_2012.csv',
     bins=np.arange(0.01, 100, 10),
     plt_type='box', cmap=cm.hot)
