# Scatter
# Scatter plots are used to visualize the relationship between two variables, often to identify patterns, clusters, or outliers in the data.

# In this example, a scatter plot visualizes the relationship between a student's study hours and their exam scores. 
# Scatter plots are well-suited for this task, as they allow the viewer to easily identify patterns or trends in the data, such as a positive correlation between study hours and exam scores.

# Here’s a short block you can place before the learning material’s plotting code so that student_performance.csv exists with realistic sample data:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random study hours between 10 and 50 for 50 students
np.random.seed(42)  # reproducible results
study_hours = np.random.randint(10, 51, size=50)

# Generate exam scores with some random variation (positive correlation with study hours)
exam_scores = np.clip(study_hours * 2 + np.random.normal(0, 15, size=50), 0, 100)

# Create DataFrame
df_students = pd.DataFrame({
    "Study_Hours": study_hours,
    "Exam_Score": exam_scores.round(1)
})

# Save to CSV so the learning material code can load it
df_students.to_csv("student_performance.csv", index=False)
print("Sample student_performance.csv file created.")

# Load student performance data
df = pd.read_csv('student_performance.csv')

# Create the scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df['Study_Hours'], df['Exam_Score'])

# Add axis labels and title
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Relationship between Study Hours and Exam Scores')

# Keep layout clean so labels aren’t cut off
plt.tight_layout()

# Save the plot
plt.savefig('scatter.png')