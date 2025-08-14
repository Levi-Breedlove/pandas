# This section presents common types of data visualizations that you can create with Matplotlib.
# Note that the following examples all use code that assumes the existence of a CSV file to read.

# Line
# Line plots are commonly used to visualize trends or changes over time, such as stock prices, temperature measurements, or population growth.

# In this example, a line plot visualizes the daily COVID-19 case numbers in a specific region over time. 
# The line plot is an effective choice, as it allows the viewer to easily identify trends and patterns in the data, such as peaks, valleys, and overall growth or decline in the number of cases.

# Here’s a short block you can place before the learning material’s plotting code so that covid_cases.csv exists with realistic sample data:

# Create fake COVID-19 case data for testing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate a date range (1 year of daily data)
dates = pd.date_range(start="2022-01-01", end="2022-12-31", freq="D")

# Generate random daily case numbers between 50 and 1000
np.random.seed(42)  # for reproducible results
cases = np.random.randint(50, 1000, size=len(dates))

# Create DataFrame
df_fake = pd.DataFrame({
    "Date": dates.strftime("%Y-%m-%d"),
    "Cases": cases
})

# Save to CSV so the learning material code can load it
df_fake.to_csv("covid_cases.csv", index=False)
print("Sample covid_cases.csv file created.")

# Load COVID-19 case data
df = pd.read_csv('covid_cases.csv')

# >>> Ensure dates behave on the x-axis <<<
import matplotlib.dates as mdates
df['Date'] = pd.to_datetime(df['Date'])

# Create the line plot
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Cases'])

# Add axis labels and title
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.title('COVID-19 Daily Cases in XYZ Region')

# >>> Make ticks look like (monthly, YYYY-MM) <<<
ax = plt.gca()
ax.xaxis.set_major_locator(mdates.MonthLocator())                 # one tick per month
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))       # format like 2022-01
# Optional: rotate a touch if your labels are tight
# plt.xticks(rotation=0)

# Keep layout clean so labels aren’t cut off
plt.tight_layout()

plt.savefig('line.png')
