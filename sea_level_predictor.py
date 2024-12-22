import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.plot(x, y, 'o', label = 'original data')

    # Create first line of best fit
    res_one = linregress(x, y)
    prediction_years = list(range(1880, 2051))
    plt.plot(prediction_years, [res_one.intercept + res_one.slope * year for year in prediction_years], 'r', label='fitted line from 1880')

    # Create second line of best fit
    df_recent_years = df[df['Year'] >= 2000]
    x_recent_years = df_recent_years['Year']
    y_recent_years = df_recent_years['CSIRO Adjusted Sea Level']
    res_two = linregress(x_recent_years, y_recent_years)
    prediction_recent_years = list(range(2000, 2051))
    plt.plot(prediction_recent_years, [res_two.intercept + res_two.slope * year for year in prediction_recent_years], 'b', label='fitted line from 2000')

    # Add labels and title
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()