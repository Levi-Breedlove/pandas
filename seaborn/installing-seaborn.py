# Official releases of Seaborn can be installed from PyPI using pip, as shown in the following code snippet.
# pip install seaborn

# You then access the library using the import command, as shown here.
# import seaborn as sns

# Once you have Seaborn installed, you’re ready to get started. 
# To test it out, you could load and plot one of the example datasets that comes with Seaborn, 
# as shown in the following example code about penguins species.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins")
sns.pairplot(df, hue="species")

# Save the plot
plt.savefig('penguin.png')

# The resulting graph is a matrix of scatter plots, where each subplot represents the relationship between two variables in the dataset. 
# The main diagonal of the matrix shows the distribution of each variable, often displayed as a histogram.

