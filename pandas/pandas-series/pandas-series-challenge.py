# Now, it’s your turn to create a pandas Series! 
# Create a pandas Series about the price of olive oil from January to September 2023 using the following pricing data.
# 136.50
# 142.03
# 144.00
# 146.44
# 148.31
# 151.60
# 156.49
# 165.76
# 175.32

import pandas as pd


olive_oil = ['136.50', '142.03', '144.00', '146.44', '148.31', '151.60', '156.49', '165.76', '175.32']

oil_price = pd.Series(olive_oil)

print(oil_price)

#or



# Olive oil prices (Jan–Sep 2023)
olive_oil = [136.50, 142.03, 144.00, 146.44, 148.31, 151.60, 156.49, 165.76, 175.32]

# Month labels
months = [
    "January", "February", "March", "April", "May", 
    "June", "July", "August", "September"
]

# Create pandas Series with months as index
oil_price = pd.Series(olive_oil, index=months)

print(oil_price)