"""
Visualizing categorical data
----------------------------
There are two ways to visualize categorical data with Seaborn. 
Categorical data is a type of data that can be divided into groups or categories. 
Examples of categorical data are nominal data (for example, favorite color) 
and ordinal data (for example, customer satisfaction levels).

Categorical scatter plot:
A categorical scatter plot visualizes the relationship between a continuous and a categorical variable, 
as shown in the following code snippet.

    sns.catplot(x="day", y="total_bill", hue="time", kind="scatter", data=tips)

This example categorical scatter plot displays the individual data points of a numerical variable 
(in this case, total_bill) for each category of a categorical variable (in this case, day). 
This can be useful for visualizing the underlying distribution of data, especially when there are many data points. 

Categorical bar plot:
A categorical bar plot visualizes the mean of a variable for different categories, 
as shown in the following code snippet.

    sns.catplot(x="day", y="total_bill", hue="time", kind="bar", data=tips)

This example categorical bar plot is similar to the regular bar plot, 
but it allows you to visualize the distribution of a numerical variable (in this case, total_bill) 
across different categories (in this case, day). 
This can help identify trends or differences in data.
"""

"""
Visualizing categorical data with hue='time'
-------------------------------------------
- Categorical data = variables that represent groups (e.g., day of week).
- We'll compare the numeric variable 'total_bill' across 'day', and split each day by meal 'time' (Lunch/Dinner).

Two plots:
1) Categorical scatter (strip) — shows all individual points, split by 'time'.
2) Categorical bar — shows the mean total_bill per day and meal, with confidence intervals.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# Load your data
# ==============================
# Option 1: Built-in dataset (ready to run)
tips = sns.load_dataset("tips")

# Option 2: Your CSV (uncomment to use)
# tips = pd.read_csv("my_data.csv")
# Your CSV must include: day (categorical), total_bill (numeric), time (categorical, e.g., Lunch/Dinner)
# Example CSV:
# day,total_bill,time
# Thur,17.50,Lunch
# Thur,18.20,Dinner
# Fri,15.70,Lunch
# Sat,22.10,Dinner
# If your headers differ, rename them:
# tips = tips.rename(columns={"YourDay":"day","Amount":"total_bill","Meal":"time"})

# ==============================
# Categorical Scatter (strip) with hue=time
# ==============================
g_scatter = sns.catplot(
    x="day",
    y="total_bill",
    hue="time",          # Lunch vs Dinner
    kind="strip",        # scatter-like plot for categorical axes; use "swarm" to avoid overlaps
    dodge=True,          # separate Lunch/Dinner points side-by-side at each day
    data=tips,
    height=5, aspect=1.3
)

# Proper title handling for catplot (FacetGrid)
g_scatter.fig.suptitle("Categorical Scatter Plot of Total Bill by Day (Hue: time)", fontsize=14)
g_scatter.fig.subplots_adjust(top=0.9)  # ensure the title isn’t clipped

# Save and (optionally) show
g_scatter.savefig("categorical_scatter_time.png")
plt.show()

# ==============================
# Categorical Bar with hue=time
# ==============================
g_bar = sns.catplot(
    x="day",
    y="total_bill",
    hue="time",          # Lunch vs Dinner
    kind="bar",          # shows the mean by default + 95% CI
    data=tips,
    height=5, aspect=1.3
)

g_bar.fig.suptitle("Categorical Bar Plot of Total Bill by Day (Hue: time)", fontsize=14)
g_bar.fig.subplots_adjust(top=0.9)

g_bar.savefig("categorical_bar_time.png")
plt.show()

