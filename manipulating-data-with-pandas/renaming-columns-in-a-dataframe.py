# Here are some reasons why you might want to rename a column in a DataFrame.

# Improve readability: 
# Column names that are too long, ambiguous, or use inconsistent naming conventions can make your data difficult to work with. 
# Renaming columns to be more descriptive and user friendly can improve the readability and understanding of data.

# Standardize naming conventions: 
# If you have data from multiple sources or data that was created by different teams, the column names might not be consistent. 
# Renaming columns to follow a standard naming convention can help streamline data processing and analysis workflows.

# Prepare data for downstream processing: 
# When integrating your data with other systems or tools, the column names might need to match specific requirements or conventions. 
# Renaming columns to meet specifications can help ensure a smooth integration process.

# Enhance data exploration: 
# During the exploratory data analysis phase, you might want to rename columns to have more intuitive or meaningful names. 
# Meaningful names help you understand data and communicate your findings.

# The rename() method is used to rename columns and passes a dictionary as the argument, where the keys are the current column names and 
# the values are the new column names. 
# In this example, the 'First Name' column is renamed as 'Firstname', and 'Last Name' is renamed as 'Lastname'. 
# The rename() method returns a new DataFrame with the columns renamed, so the result is assigned back to the DataFrame.


import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'First Name': ['John', 'Jane', 'Bob', 'Alice'], 
                   'Last Name': ['Doe', 'Smith', 'Johnson', 'Williams'],
                   'Age': [25, 32, 28, 30]})

# Observe the initial DataFrame
print(df)

# Rename the columns
df = df.rename(columns={'First Name': 'Firstname', 
				'Last Name': 'Lastname'})

# Observe the output
print(df)