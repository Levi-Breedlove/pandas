import pandas as pd


# Define a dictionary containing airline origin information.

airline_origin = {

"Airline": ['Airline1', 'Airline2', 'Airline3', 'Airline4', 'Airline5', 'Airline6'],

"Origin": ['BOS', 'ESR', 'FRA', 'YVC', 'MAD', 'DUB'],

"Flight number": ['US9876', 'FS2345', 'SA5678', 'CA1357', 'AZ7880', 'DB7986']

}

# Print the dictionary.

print('Original Data:', airline_origin)

# Print the type of data.

print(type(airline_origin))


# Create a DataFrame using the dictionary.

df = pd.DataFrame(airline_origin)


# Print the DataFrame.

print(df)