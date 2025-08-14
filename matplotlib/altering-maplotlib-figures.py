# Several important elements can be added to a figure to help make the purpose of the visualization clearer, as described in the following tabs.

# Single, runnable script that mirrors the learning material,
# creates stock_prices.csv if missing, and outputs three plots.

# It saves PNGs (for headless/script environments). If you're in Jupyter,
# you can replace each savefig/close with plt.show().

import os
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # headless-friendly
import matplotlib.pyplot as plt

# ---------- Setup: create stock_prices.csv if not present ----------
csv_path = "stock_prices.csv"
if not os.path.exists(csv_path):
    dates = pd.date_range(start="2022-01-01", periods=365, freq="D")
    any_prices = (100 + np.cumsum(np.random.randn(365))).round(2)
    example_prices = (95 + np.cumsum(np.random.randn(365))).round(2)

    df_setup = pd.DataFrame({
        "Date": dates.strftime("%Y-%m-%d"),  # keep as strings to mirror material
        "Price": any_prices,                 # single-company series used in Axis/Title
        "Any": any_prices,                   # multi-company columns for Legend example
        "Example": example_prices
    })
    df_setup.to_csv(csv_path, index=False)

# Axis:
# Adding axis labels to a Matplotlib plot helps provide context and make the data more interpretable for viewers. 
# This is particularly important when visualizing complex datasets or when the axes represent specific units of measurement.
# The following example shows the code for a plot that visualizes a company's daily stock price over the course of a year. 
# The code example shows how to add axis labels that indicate the x-axis as Date and the y-axis as Price (USD).

# ---------- Example 1: Axis labels ----------
df = pd.read_csv(csv_path)

plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Price'])
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.tight_layout()
plt.savefig("example_axis_labels.png")
plt.close()



# Title:
# Adding a descriptive title to a Matplotlib plot helps communicate the main purpose or focus of a visualization. 
# This can be particularly useful when creating a series of related plots or when presenting a visualization to an audience.
# Continuing the stock price example, the following code shows how to add a title to the plot to clearly indicate the company and time period.
# import matplotlib.pyplot as plt
# import pandas as pd

# ---------- Example 2: Title ----------
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Price'])
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('AnyCompany Stock Prices (2022)')
plt.tight_layout()
plt.savefig("example_title.png")
plt.close()



# Legend:
# Adding a legend to a Matplotlib plot can help viewers understand the various elements or data series being displayed. 
# This is particularly useful when creating visualizations with multiple lines, bars, or other graphical elements.
# Suppose you're creating a plot to compare the stock prices of multiple companies. 
# You would want to add a legend to clearly indicate which line corresponds to each company.
# import matplotlib.pyplot as plt
# import pandas as pd

# ---------- Example 3: Legend ----------
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Any'], label='AnyCompany')
plt.plot(df['Date'], df['Example'], label='Example Corporation')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('Stock Price Comparison')
plt.legend()
plt.tight_layout()
plt.savefig("example_legend.png")
plt.close()

print("Created files: stock_prices.csv, example_axis_labels.png, example_title.png, example_legend.png")




