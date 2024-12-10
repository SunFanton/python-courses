import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    data = pd.read_csv("epa-sea-level.csv")

    plt.subplots(figsize=(15,7))
    
    # Create scatter plot
    plt.scatter(x=data["Year"], y=data["CSIRO Adjusted Sea Level"], alpha=0.5, zorder=3)
    
    # Create first line of best fit
    resul = linregress(x=data["Year"], y=data["CSIRO Adjusted Sea Level"])
    slope = resul.slope
    intercept = resul.intercept
    line_y = data["Year"] * slope + intercept
    plt.plot(data["Year"], line_y, color="red", linestyle="dashed", zorder=4)

    # Create second line of best fit
    recent_years = data[data["Year"] >= 2000]
    resul_recent_years = linregress(x=recent_years["Year"], y=recent_years["CSIRO Adjusted Sea Level"])
    slope_recent_years = resul_recent_years.slope
    intercept_recent_years = resul_recent_years.intercept
    array = np.arange(recent_years["Year"].min()+1, 2051, 1)
    recent_years_and_beyond = np.concatenate((recent_years["Year"].to_numpy(), array))
    line_y_recent_years_and_beyond = recent_years_and_beyond * slope_recent_years + intercept_recent_years
    plt.plot(recent_years_and_beyond, line_y_recent_years_and_beyond, color="orange", zorder=5)
    
    # Add labels and title
    plt.yticks(np.arange(int(data["CSIRO Adjusted Sea Level"].min() - 1), \
                     int(line_y_recent_years_and_beyond.max() + 1), \
                     0.5))
    plt.xticks(np.arange(int(data["Year"].min()), \
                         recent_years_and_beyond.max() + 1, \
                         10))
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.grid(True, zorder=0)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()