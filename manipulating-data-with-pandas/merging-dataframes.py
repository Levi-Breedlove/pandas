# Merging DataFrames is a common operation in data analysis and data processing workflows. 
# You might need to merge DataFrames for a variety of reasons.

# Integrate data from multiple sources: 
# If you have data stored in separate DataFrames, merging them can help you combine the information into a single, more comprehensive dataset.

# Enrich data with additional information: 
# You can merge a DataFrame containing core data with another DataFrame that has supplementary information, 
# such as customer details or product specifications.

# Perform relational queries: 
# Merging DataFrames allows you to run SQL-like queries, such as inner joins, outer joins, or left/right joins, 
# to connect related data based on common columns or indices.

# Prepare data for modeling: 
# Before training an ML model, you might want to merge multiple DataFrames to create a unified dataset 
# that includes all the features and target variables required for your analysis.

# This example starts with two DataFrames, customers and orders. 
# The merge() method is used to combine the two DataFrames. 
# The customers and orders DataFrames are passed as the first two arguments, and specify the column to use for the merge operation.

# In this example, it is 'CustomerID' using the on parameter. 
# The how='inner' argument tells Pandas to perform an inner join, meaning that only the rows with matching CustomerID values 
# in both DataFrames will be included in the merged result. 

# After calling the merge() function, the resulting merged DataFrame contains the combined data from both the customers and 
# orders DataFrames, with the relevant columns from each DataFrame included.


import pandas as pd

# Create two sample DataFrames
customers = pd.DataFrame({'CustomerID': [1001, 1002, 1003, 1004],
                          'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Williams'],
                          'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']})

orders = pd.DataFrame({'OrderID': [100, 101, 102, 103],
                       'CustomerID': [1001, 1002, 1003, 1004],
                       'Total': [250.00, 150.75, 300.50, 175.25]})
                       
# Observe intiial DataFrames
print(customers)
print(orders)

# Merge the DataFrames based on the 'CustomerID' column
merged_df = pd.merge(customers, orders, on='CustomerID', how='inner')

# Observe the output
print(merged_df)