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

print('DataFrame:\n', df)


# Store and display the first two rows.

airline_head = df.head(2)

print('First two rows:\n', airline_head)


# Store and display the last two rows.

airline_tail = df.tail(2)

print('Last two rows:\n', airline_tail)