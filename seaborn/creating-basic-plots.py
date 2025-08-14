# ===Scatter plot:===

# A scatter plot visualizes a relationship between two continuous variables.
# sns.scatterplot(x="total_bill", y="tip", data=tips)

# This example scatter plot shows the relationship between two numerical variables (total_bill and tip).
# It plots individual data points to let you visually inspect distribution and correlation.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===== Load data =====
# Option 1: Use Seaborn's built-in dataset (fast & ready to run)
tips = sns.load_dataset("tips")

# Option 2: Load your own CSV data (uncomment and edit file path)
# tips = pd.read_csv("my_tips_data.csv")
# Example CSV for scatter plot:
# total_bill,tip
# 24.50,4.00
# 15.20,3.10
# 42.00,8.50

# ===== Create the scatter plot =====
sns.scatterplot(x="total_bill", y="tip", data=tips)

# Add title
plt.title("Scatterplot of Total Bill vs Tip")

# Show plot first
plt.show()

# Save plot to file
plt.savefig("scatter.png")

# ===END Scatter plot:===



# ===Line plot:===

# A line plot visualizes the trend of a variable over time or another ordered variable.
# This example uses 'signal' over 'timepoint', grouped by 'region'.

# Useful for visualizing time-series data or comparing trends between groups.

# ===== Load data =====
# Option 1: Use built-in fmri dataset
fmri = sns.load_dataset("fmri")

# Option 2: Load your own CSV (uncomment below)
# fmri = pd.read_csv("my_fmri_data.csv")
# Example CSV for line plot:
# timepoint,signal,region
# 0,0.02,frontal
# 0,0.01,parietal
# 1,0.04,frontal
# 1,0.03,parietal

# ===== Create line plot grouped by category =====
plt.figure(figsize=(8, 6))
sns.lineplot(x="timepoint", y="signal", hue="region", data=fmri)

# Add labels & title
plt.title("Line Plot of Signal over Time by Region")
plt.xlabel("timepoint")
plt.ylabel("signal")

# Save & show
plt.savefig("lineplot_signal_region.png")
plt.show()

# ===END Line plot:===



# ===Bar plot:===

# A bar plot visualizes the mean of a variable for each category.
# This example shows average total_bill for each day.

# ===== Load data =====
# Option 1: Use built-in tips dataset
tips = sns.load_dataset("tips")

# Option 2: Load your own CSV (uncomment below)
# tips = pd.read_csv("my_bar_data.csv")
# Example CSV for bar plot:
# day,total_bill
# Thur,17.50
# Thur,18.20
# Fri,15.70
# Sat,22.10

# ===== Create bar plot =====
plt.figure(figsize=(8, 6))
sns.barplot(x="day", y="total_bill", data=tips)

# Add title & axis labels
plt.title("Bar Plot of Average Total Bill by Day")
plt.xlabel("day")
plt.ylabel("total_bill")

# Save & show
plt.savefig("barplot_avg_totalbill.png")
plt.show()

# ===END Bar plot:===
