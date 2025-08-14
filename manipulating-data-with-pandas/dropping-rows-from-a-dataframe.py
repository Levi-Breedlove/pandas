# At times, you might want to drop a row from a DataFrame. 
# Here are some reasons why.

# Remove outliers or erroneous data: 
# If your dataset contains outliers or data points that are clearly erroneous, 
# you might want to drop those rows to prevent them from skewing your analysis or model training.

# Filter for specific conditions: 
# You might need to remove rows that don't meet certain criteria. 
# For example, you might want to drop all rows where the 'Age' column is below 18 to focus your analysis on adult data.

# Handle missing data: 
# If your DataFrame contains rows with missing values that you can't or don't want to impute, 
# you might choose to drop those rows to ensure your analysis is based on complete data.

# Subset a dataset: 
# You might want to work with a smaller, more manageable subset of your data, 
# so you want to drop rows that are not relevant to your current task or analysis.

# In this example, the drop() method is used to drop a specific row from the DataFrame, 
# passing the index of the row you want to remove, in this case, 1. 

# The drop() method returns a new DataFrame with the specified row removed, so the result is assigned back to the DataFrame.

import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob', 'Alice'], 
			'Age': [25, 32, 28, 30]})

# Observe the initial DataFrame
print(df)

# Drop the row with index 1
df = df.drop(1)

# Observe the output
print(df)