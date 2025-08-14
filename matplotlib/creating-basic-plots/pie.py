# Pie:
# Pie charts are used to show the proportional sizes of different categories or components in a whole.
# In this example, a pie chart visualizes the market share of different smartphone brands in a particular region.
# Pie charts are well-suited for this type of data, as they allow the viewer to quickly understand the relative proportions of each brand's market share.

# Market share data is basically a snapshot of how much of a total market each company or product controls, expressed as a percentage of the whole.
# Think of the market as a big pie — market share is the slice each competitor owns.

# For example, if the smartphone market in a given year sold 1 million units total:
# Brand A sold 220,000 → 22% market share
# Brand B sold 240,000 → 24% market share
# Brand C sold 120,000 → 12% market share
# Brand D sold 240,000 → 24% market share
# Brand E sold 180,000 → 18% market share

# Why it matters:
# Business performance – Shows who’s leading and who’s falling behind.
# Trend spotting – Reveals how customer preferences shift over time.
# Strategy – Companies use it to target growth or defend their position.

# In your pie chart example, we’re not using real sales figures — 
# we’re just creating fake but realistic percentages so you can see how the code works. 
# The sum of all percentages is 100%, because it represents the entire market.

# -------------------------------------------------------
# Create sample smartphone_market_share.csv file first
# -------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Sample smartphone market share data
market_data = {
    "Brand": ["Brand A", "Brand B", "Brand C", "Brand D", "Brand E"],
    "Market_Share": [22, 24, 12, 24, 18]  # values sum to 100%
}

# Save to CSV
df_market = pd.DataFrame(market_data)
df_market.to_csv("smartphone_market_share.csv", index=False)
print("Sample smartphone_market_share.csv file created.")

# -------------------------------------------------------
# Learning material plotting code
# -------------------------------------------------------

# Load market share data for smartphone brands
df = pd.read_csv('smartphone_market_share.csv')

# Create the pie chart
plt.figure(figsize=(8, 6))
plt.pie(df['Market_Share'], labels=df['Brand'], autopct='%1.0f%%')

# Add a title
plt.title('Smartphone Market Share')

# Save the figure
plt.savefig('pie.png')
print("pie.png saved.")
