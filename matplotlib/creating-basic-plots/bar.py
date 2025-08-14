# Bar:
# Bar plots are commonly used to compare values or categories, such as sales figures across different products or average test scores for different student groups.
# In this example, a bar plot is used to compare the average annual salaries for different job roles in a company. 
# Bar plots are a suitable choice, as they allow the viewer to easily compare the values for each category (job role) and identify any significant differences or patterns.

# -------------------------------------------------------
# Create sample salaries.csv file before running plot code
# -------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

# Create sample salary data
salary_data = {
    "Job_Role": ["Manager", "Engineer", "Analyst", "Developer", "Designer"],
    "Average_Salary": [70000, 102000, 117000, 84000, 94000]
}

# Save the dataset to CSV
df_salaries = pd.DataFrame(salary_data)
df_salaries.to_csv("salaries.csv", index=False)
print("Sample salaries.csv file created.")

# -------------------------------------------------------
# Learning material plotting code
# -------------------------------------------------------

# Load salary data for different job roles
df = pd.read_csv('salaries.csv')

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Job_Role'], df['Average_Salary'])

# Add axis labels and title
plt.xlabel('Job Role')
plt.ylabel('Average Salary (USD)')
plt.title('Average Annual Salaries by Job Role')

# Ensure layout fits well
plt.tight_layout()

# Save the figure
plt.savefig('bar.png')
print("bar.png saved.")
