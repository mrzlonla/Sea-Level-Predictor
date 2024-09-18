import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Import data
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
    
    # Create first line of best fit
    result = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = pd.Series(range(df['Year'].min(), 2051))
    y = result.intercept + result.slope * x
    plt.plot(x, y, color='red', label='Fit Line (1880-present)')
    
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    y_recent = result_recent.intercept + result_recent.slope * x
    plt.plot(x, y_recent, color='green', label='Fit Line (2000-present)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save and show plot
    plt.savefig('sea_level_plot.png')
    plt.show()

draw_plot()
