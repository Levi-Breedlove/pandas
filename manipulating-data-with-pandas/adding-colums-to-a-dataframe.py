# There are three methods that you can use to add a new column to a DataFrame. 
# In each of the following examples, an initial dictionary called product_data is created that contains sample 
# product data with three columns, 'Product', 'Price', and 'Category'. 

# The dictionary is then converted into a pandas DataFrame. 
# You will review three ways a new column, 'Warranty', can be added. 

# Here are some reasons why you might add a column to a DataFrame.
# Feature engineering: You might want to create new columns that represent derived features or transformations of your existing data, 
# which can improve the performance of your ML models.

# Data integration: When combining data from multiple sources, you might need to add new columns to your DataFrame to incorporate the 
# additional information.

# Exploratory data analysis: During the data exploration phase, you might add new columns to your DataFrame to investigate relationships, 
# test hypotheses, or create visualizations.

# Data enrichment: You can add columns to your DataFrame to supplement the existing data with additional context, metadata, or other relevant information.

# insert()
# The insert() method allows you to add a new column at a specific index in a DataFrame, rather than appending it to the end of the DataFrame. 
# This can be helpful when you need to preserve the order of existing columns.
# In this example, a list is declared, called warranty_periods, which contains the warranty periods in years for each product. 
# The insert() method is used, specifying 1 as the index for where the new column should be inserted. 
# This places it between the 'Product' and 'Price' columns.


# Import pandas package
import pandas as pd

# Define a dictionary containing product data
product_data = {
	'Product': ['Laptop', 'Smartphone', 'Tablet', 'Desktop'],
	'Price': [999.99, 499.99, 299.99, 799.99],
	'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(product_data)

# Declare a list of warranty periods (in years)
warranty_periods = [2, 1, 1, 3]

# Add the 'Warranty' column using the insert() method
df.insert(1, 'Warranty', warranty_periods)

# Observe the output
print(df)

print() #whitespace

# assign()
# The assign() method is useful when you want to add a new column and potentially perform other transformations to the DataFrame at the same time.
# In this example, a new dictionary, called warranty_periods, is created that maps the product names to their respective warranty periods. 
# The assign() method is then used to create the new 'Warranty' column, applying the warranty_periods dictionary to the 'Product' column using the map() function. 
# The assign() method returns a new DataFrame with the added column, so the result is assigned back to the DataFrame.


# Define a dictionary containing product data
product_data = {
	'Product': ['Laptop', 'Smartphone', 'Tablet', 'Desktop'],
	'Price': [999.99, 499.99, 299.99, 799.99], 
	'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(product_data)

# Declare a dictionary of warranty periods (in years)
warranty_periods = {'Laptop': 2, 'Smartphone': 1, 'Tablet': 1, 'Desktop': 3}

# Add the 'Warranty' column using the assign() method
df = df.assign(Warranty=df['Product'].map(warranty_periods))

# Observe the output
print(df)

print() #whitespace

# loc()
# The loc() method offers fine-grained control over the addition of a new column. 
# It is useful for complex data manipulation scenarios, where you need to select specific rows or columns and perform operations on them.

# To add the new 'Warranty' column, the loc[] accessor is used to select all rows (:) and the new column name 'Warranty'. 
# They are then assigned a list of warranty periods, [2, 1, 1, 3].


# Define a dictionary containing product data
product_data = {
	'Product': ['Laptop', 'Smartphone', 'Tablet', 'Desktop'],
	'Price': [999.99, 499.99, 299.99, 799.99], 
	'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(product_data)

# Add the 'Warranty' column using the loc() method
df.loc[:, 'Warranty'] = [2, 1, 1, 3]

# Observe the output
print(df)






