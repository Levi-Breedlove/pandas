# One of the primary advantages of pandas is data alignment. 
# pandas DataFrames are organized into easy-to-read tabular formats.

# This intrinsic property enhances readability and means that data analysts can perform operations quickly and efficiently.

# The pandas Series refers to a column of homogeneous data within a DataFrame. 
# This data can be any type, such as strings, integers, or floats. 
# There are many ways to create a pandas Series. 
# For example, you can use a Python list, N-dimensional array (ndarry), or Python dictionary.

# An ndarray, also called a NumPy array, is a fundamental data structure in the NumPy library for Python. 
# It represents a collection of elements, all of the same data type, organized in a multidimensional grid. 
# The key features of an ndarray are its ability to efficiently store and operate on large amounts of data, and its support for a wide range of mathematical and scientific computations. 

# The following code sample demonstrates how to create a pandas Series. 
# In this code, the following steps happen.
# An array is created that contains movie genres.
# The pandas Series method pd.Series is called and passes the movie genres array.
# The Series is printed.

# Output:
# The output has the following characteristics when you run the code:
# A pandas Series object with its index (0, 1, 2, 3, 4) and the corresponding values from the genres list ('Horror', 'Comedy', 'Thriller', 'Romance', 'Sci-Fi')
# pandas automatically outputs the data type when printing the Series.


import pandas as pd
genres = ['Horror', 'Comedy', 'Thriller', 'Romance', 'Sci-Fi']

# Create a pandas series.
series = pd.Series(genres)

# Print the series.
print(series)