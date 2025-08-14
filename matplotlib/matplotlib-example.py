# Now that you know the basics, you're ready to explore visualizations with a use case example. 
# In the following code snippet, you can see a pandas DataFrame containing airline ticket prices between two cities from eight airline companies in 2022 and 2023.

import pandas as pd
import matplotlib.pyplot as plt
ticket_price = { "2022": ['$175', '$210', '$275', '$480', '$180', '$187', '$190', '$229'], "2023":['$179','$205', '$295', '$520', '$199', '$199', '$211', '$250']}

df = pd.DataFrame(ticket_price, columns=["2022", "2023"], index=["Airline1", "Airline2", "Airline3", "Airline4", "Airline5", "Airline6", "Airline7", "Airline8"])

# Print the DataFrame.
print(df)

# To compare the prices, you can convert the DataFrame into a simple line graph. 
# Review the following code, which creates a line graph comparing airline ticket prices between 2022 and 2023 for different airline companies.

# import pandas as pd
# import matplotlib.pyplot as plt

ticket_prices = {

   '2022': ['175', '210', '275', '480', '180', '187', '190', '229'],

   '2023': ['179', '205', '295', '520', '199', '199', '211', '250']

}

# Create a DataFrame with index values

df = pd.DataFrame(ticket_prices, columns=['2022', '2023'], index=['Airline1', 'Airline2', 'Airline3', 'Airline4', 'Airline5', 'Airline6', 'Airline7', 'Airline8'])

# Convert the year values to integer

df['2022'] = df['2022'].astype(int)

df['2023'] = df['2023'].astype(int)

# Create the figure and axis objects

fig, ax = plt.subplots(figsize=(12, 6))

# Create the categorical bar graph

x = range(len(df.index))

width = 0.4

ax.bar([i - width/2 for i in x], df['2022'], width=width, label='2022')

ax.bar([i + width/2 for i in x], df['2023'], width=width, label='2023')

# Set the x-axis tick labels

ax.set_xticks(x)

ax.set_xticklabels(df.index)

# Set the title and axis labels

plt.title("Airline ticket prices")

plt.xlabel("Airline companies")

plt.ylabel("Prices")

# Add a legend

plt.legend()

# Save the plot to the file system

plt.savefig('airline-ticket-prices-bar-graph.png')

# When you run the code, Matplotlib produces a comprehensive two-line graph, as expected, and saves it to the filesystem as airline-ticket-prices-bar-graph.png.
# The x-axis shows the airline company names.
# The y-axis shows the prices of the airline tickets for 2022 and 2023.
# The graph displays the legend and title. 
# The line graph provides an effective visualization of an overview of the data. 
# The developer can clearly see that most prices have increased between 2022 and 2023.




