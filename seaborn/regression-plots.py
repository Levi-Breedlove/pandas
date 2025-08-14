"""
Regression plots
----------------
There are two ways to visualize regression plots with Seaborn. 
Regression plots are a type of data visualization used to visualize the relationship among two or more variables, typically a dependent variable (y-axis) and one or more independent variables (x-axis). 
These plots help you understand the strength and direction of a linear or nonlinear relationships among variables.

Regression plot:
A regression plot visualizes a linear relationship between two variables and the confidence interval, as shown in the following code snippet.
    sns.regplot(x="total_bill", y="tip", data=tips)

This example regression plot shows the relationship between two numerical variables (in this case, total_bill and tip) by fitting a linear regression line and displaying individual data points. 
This helps assess the strength and direction of the linear relationship between the variables. 

Residual plot:
A residual plot visualizes the residuals from a linear regression model, as shown in the following code snippet.
    sns.residplot(x="total_bill", y="tip", data=tips)

This example residual plot displays the residuals (the difference between the observed values and the predicted values from a regression model) against the predictor variable (in this case, total_bill). 
This can be useful for checking the assumptions of a regression model, such as linearity and homoscedasticity.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# Load your data
# ==============================
# Option 1: Built-in dataset (ready to run)
tips = sns.load_dataset("tips")

# Option 2: Your CSV (uncomment to use)
# tips = pd.read_csv("my_tips_data.csv")
# Your CSV must include at least these columns:
#   total_bill,tip
# Example CSV rows:
#   24.50,4.00
#   15.20,3.10
#   42.00,8.50
# If your headers differ, rename them:
# tips = tips.rename(columns={"Amount":"total_bill","Gratuity":"tip"})

# ==============================
# Regression plot
# ==============================
plt.figure(figsize=(8, 6))
sns.regplot(x="total_bill", y="tip", data=tips)
plt.title("Regression Plot of Tip vs Total Bill")
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.tight_layout()                 # prevent any clipping
plt.savefig("regplot_tip_totalbill.png")
plt.show()

# ==============================
# Residual plot
# ==============================
plt.figure(figsize=(8, 6))
sns.residplot(x="total_bill", y="tip", data=tips)
plt.title("Residual Plot of Tip vs Total Bill")
plt.xlabel("total_bill")
plt.ylabel("tip")
plt.axhline(0, ls="--", c="k", lw=1, alpha=0.6)  # zero baseline for reference
plt.tight_layout()
plt.savefig("residplot_tip_totalbill.png")
plt.show()