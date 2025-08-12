# To return information about a DataFrame with mixed data types, you can use .describe(). 
# The output returns the count, unique, top, and frequency values.

# Input:
# The following DataFrame includes the number of passengers and baggage details on each flight. 
# In the code sample, notice how the .describe() method works.

import pandas as pd

airline_origin = {
	"Airline": ['Airline1', 'Airline2', 'Airline3', 'Airline4'],
	"Origin": ['BOS', 'ESR', 'FRA', 'YVC'],
	"Passengers": ['402', '370', '367', '398'],
	"Baggage": ['580', '701', '432', '508']
}

df = pd.DataFrame(airline_origin)

# Print the DataFrame.
print('DataFrame:\n',df)

# Display statistics of the data.
summarize = df.describe()

print('Statistics:\n',summarize)

