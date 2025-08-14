# Adding rows to a DataFrame:
# There are two methods that you can use to add a new row to a DataFrame. 
# Here are some reasons why you might need to add rows to a DataFrame.

# Data ingestion and collection: 
# When building data pipelines or integrating with external data sources, you might need to continuously 
# add new rows to your DataFrame as the data is collected or ingested.

# Missing data imputation: 
# If your DataFrame has missing values, you might want to add new rows to represent those missing data points, 
# either by imputing the values or by creating placeholder rows for further processing.

# Manual data entry or correction: 
# You might need to manually add or update rows in your DataFrame, for example, to correct errors, add new information, 
# or incorporate feedback from subject matter experts.

# Synthetic data generation: 
# In the context of machine learning (ML), you might want to add new, synthetically generated rows to your DataFrame to 
# expand the size and diversity of your training data.

# concat():
# When you have an existing pandas DataFrame, you can use concat() with data that you want to add as new rows. 
# This is useful when you need to combine data from multiple sources or add multiple rows at once. 
# Additionally, it provides more flexibility compared to appending a single Series.

# In this example, there are two initial DataFrames, df1 and df2, each with two rows of data and organized in two columns, 'Name' and 'Age'. 
# The concat() method is used to add the rows from df2 to df1. 
# This passes both DataFrames as a list [df1, df2] as the first argument. 
# The ignore_index=True parameter tells pandas to assign new indices to the resulting DataFrame, rather than preserving the original indices.

import pandas as pd

# Create a sample DataFrame
df1 = pd.DataFrame({'Name': ['John', 'Jane'],  
			'Age': [25, 32]})

# Create another sample DataFrame
df2 = pd.DataFrame({'Name': ['Bob', 'Alice'],
			'Age': [28, 30]})

# Concatenate the DataFrames
df = pd.concat([df1, df2], ignore_index=True)

# Observe the output
print(df)

#output:
#     Name  Age
# 0   John   25
# 1   Jane   32
# 2    Bob   28
# 3  Alice   30

print( ) #white space

# loc[]
# You use the loc[] method when you want to create a new row from scratch, without an existing Series or DataFrame. 
# This method should also be used when you need to add a new row at a specific index, rather than appending to the end.

# In this example, an initial DataFrame is created that contains three rows of data, organized in two columns, 'Name' and 'Age'. 
# The loc[] accessor adds a new row to the DataFrame. 

# The expression len(df) provides the current number of rows, which is then used to obtain the index for the new row. 
# Next, a list containing the new values, ['Alice', 30], is assigned to the new index, which creates a new row in the DataFrame.


# Create a sample DataFrame
df = pd.DataFrame({'Name': ['John', 'Jane', 'Bob'],         
			'Age': [25, 32, 28]})

# Add a new row using loc
df.loc[len(df)] = ['Alice', 30]

# Observe the output
print(df)

