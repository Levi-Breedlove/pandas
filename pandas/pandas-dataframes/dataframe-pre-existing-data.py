import pandas as pd
# Create a list of lists
airline_data = [['Airline1', 'Domestic', 100],
		['Airline2', 'International', 200],
		['Airline3', 'Domestic', 150],
		['Airline4', 'International', 300],
		['Airline5', 'Domestic', 120],
		['Airline6', 'International', 250]]

# Create a DataFrame from the list of lists
df = pd.DataFrame(airline_data, columns=['Airline', 'Type', 'Passengers'])

# Print the DataFrame
print('Airline Data:', df)

# Print the third row
print('Third row:', df.loc[2])

# Use slicing to print the range of rows
print('Range of rows:', df.loc[2:4])