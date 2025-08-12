# This code sample also shows how to create a DataFrame from a dictionary. 
# The resulting DataFrame has column names taken from the dictionary keys, and the values are organized into rows. 
# Before manipulating the data, you can check how large the entire DataFrame is by using the attributes .ndim, .shape, and .size.

# df.ndim
# This attribute returns the number of dimensions (axes) of the DataFrame. 
# In the example, the following line will print the number of dimensions of the df DataFrame.
# print('Dimensions:', df.ndim) 
# For a 2D DataFrame, the output will be 2 (one for rows and one for columns).

# df.shape
# This attribute returns a tuple representing the DataFrame's dimensions. 
# The first element of the tuple is the number of rows, and the second element is the number of columns. 
# In the example, the following line will print the shape of the df DataFrame as a tuple (number of rows, number of columns).
# print('Shape:', df.shape) 

# df.size
# This attribute returns the total number of elements in the DataFrame. 
# It is calculated by multiplying the number of rows by the number of columns. 
# In the example, the following line of code will print the total number of elements (cells) in the df DataFrame.

# print('Size:', df.size) 
# Review the same code sample but with the addition of inspecting these attributes:
import pandas as pd

# Define a dictionary containing airline origin information.
airline_origin = {
	"Airline": ['Airline1', 'Airline2', 'Airline3', 'Airline4', 'Airline5', 'Airline6'],
	"Origin": ['BOS', 'ESR', 'FRA', 'YVC', 'MAD', 'DUB'],
	"Flight number": ['US9876', 'FS2345', 'SA5678', 'CA1357', 'AZ7880', 'DB7986']
}

# Create a DataFrame using the dictionary.
df = pd.DataFrame(airline_origin)

# Print the DataFrame.
print('DataFrame:\n',df)

# Print the dimensions.
print('Dimensions:', df.ndim)

# Print the shape.
print('Shape:', df.shape)

# Print the size of DataFrame.
print('Size:', df.size)

