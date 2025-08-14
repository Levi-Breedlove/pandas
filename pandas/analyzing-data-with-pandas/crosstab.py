# crosstab()
# The crosstab() function allows you to create a table that shows the frequency or count of observations that fall into different combinations of categories. 
# For example, if you're analyzing data on customer purchases, you might use crosstab() to create a table that shows the number of customers who bought each type of product, 
# broken down by their gender or age group.
# The crosstab() function is useful when you're trying to understand the relationships among categorical variables. 
# Categorical variables are ones that can be divided into distinct groups or categories, such as gender (male and female), marital status (single, married, and divorced), 
# or type of product (clothing, electronics, and furniture). 
# By seeing how observations are distributed across different combinations of categories, you can identify patterns and trends that might not be immediately obvious from raw data.
# The crosstab() function returns a DataFrame and, by default, computes a frequency table of the factors unless an array of values and an aggregation function are passed.
#  
# The following code snippet shows the crosstab() function and its available parameters.

# pandas.crosstab(index, columns, values=None, rownames=None, colnames=None, 
# aggfunc=None, margins=False, margins_name='All', dropna=True, normalize=False) 


# A cross-tabulation, also known as a contingency table or crosstab, is a statistical tool used to analyze the relationships among two or more categorical variables. 
# It displays the frequency distribution of the variables in a tabular format, allowing you to understand how different categories of one variable are associated with the categories of another variable.

# Tabular format:
# A cross-tabulation is presented in a table with rows representing the categories of one variable and columns representing the categories of another variable. 
# The cells of the table contain the frequency or count of observations that fall into the intersection of the corresponding row and column categories.

# Catigorical variables:
# Cross-tabulations are typically used with categorical variables, which are variables that have a finite set of distinct categories or values. 
# Examples of categorical variables include gender (male, female), education level (high school, college, graduate), or product type (electronics, apparel, home goods).

# Discovering relationships:
# By examining frequencies in a cross-tabulation table, you can identify patterns and relationships between the variables. 
# For example, you might discover that a certain age group is more likely to purchase a specific product or that there is a relationship between a customer's location and their preferred payment method.

# Statistical analysis:
# Cross-tabulations can also be used to perform statistical tests, such as the chi-square test, to determine whether an observed relationship between variables is statistically significant or likely to have occurred by chance.


# Cross-tabulations are widely used in various fields, including market research, social sciences, and business analytics, to gain a deeper understanding of the underlying relationships in datasets. 
# They provide a simple and intuitive way to visualize and analyze the associations between different categorical variables, making them a valuable tool for new software developers 
# working with data-driven applications.
# crosstab() example

import pandas as pd

# Create a sample DataFrame
data = {
	'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
	'Age Group': ['Young', 'Young', 'Middle', 'Middle', 'Old', 'Old']
}

df = pd.DataFrame(data)

print(df)

# Create a cross-tabulation
cross_tab = pd.crosstab(df['Gender'], df['Age Group'])
print(cross_tab)

# Output
# The preceding code will output the following contingency table. 
# The rows represent the categories of the 'Gender' variable, and the columns represent the categories of the 'Age Group' variable. 
# The values in the cells represent the count of observations that fall into the intersection of the corresponding row and column categories.

# Here's how you can interpret the cross-tabulation.
# There is 1 female in the Middle age group, 1 female in the Old age group, and 1 female in the Young age group.
# There is 1 male in the Middle age group, 1 male in the Old age group, and 1 male in the Young age group.

# In addition, you can add arguments to the crosstab() function, such as the following:
# normalize: Display the values as proportions instead of counts
# margins: Include row and column totals
# dropna: Remove rows or columns with missing values