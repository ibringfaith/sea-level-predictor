import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, color='purple', label = 'Original Data')

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(x, y)
    prediction_years = pd.Series(range(1880, 2051))
    best_fit = slope * prediction_years + intercept
    plt.plot(prediction_years, best_fit, label='Best Fit (1880-2050)', color='blue')

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    best_fit_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, best_fit_recent, label='Best Fit (2000-2050)', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()