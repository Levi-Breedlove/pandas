# Bootstrapping (put at the top of your script)
# Always put this first in a headless/script environment
import matplotlib
matplotlib.use("Agg")  # render to files instead of a GUI window

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Example 1 — Python lists (line plot)
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure()
plt.plot(x, y, marker="o")
plt.title("Example 1: Lists -> Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.savefig("example1_lists.png")
plt.close()
print("Saved example1_lists.png")

# Example 2 — Python dictionaries (proper unpacking)

# Fixes the incorrect items() commentary and prints what Python actually returns.

data = {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}

# Show what these produce
print("dict:", data)
print("data.items():", list(data.items()))
print("*data.items() iterates tuples; for plotting use zip(*data.items())")

# Correct unpack for plotting
xs, ys = zip(*data.items())

plt.figure()
plt.plot(xs, ys, marker="o")
plt.title("Example 2: Dict -> Line Plot")
plt.xlabel("x (keys)")
plt.ylabel("y (values)")
plt.tight_layout()
plt.savefig("example2_dict.png")
plt.close()
print("Saved example2_dict.png")

# Example 3 — pandas DataFrame columns
df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]})

plt.figure()
plt.plot(df["x"], df["y"], marker="o")
plt.title("Example 3: DataFrame Columns -> Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.savefig("example3_dataframe.png")
plt.close()
print("Saved example3_dataframe.png")

# Example 4 — Local CSV file

# If you don’t have a data.csv, we’ll create one first, then read it and plot.

# Create a sample CSV so this always runs
sample_csv = pd.DataFrame({
    "column1": [1, 2, 3, 4, 5],
    "column2": [2, 3, 5, 7, 11]
})
sample_csv.to_csv("data.csv", index=False)

# Load and plot
df_csv = pd.read_csv("data.csv")
x = df_csv["column1"]
y = df_csv["column2"]

plt.figure()
plt.plot(x, y, marker="o")
plt.title("Example 4: CSV -> Line Plot")
plt.xlabel("column1")
plt.ylabel("column2")
plt.tight_layout()
plt.savefig("example4_csv.png")
plt.close()
print("Saved example4_csv.png (and wrote data.csv)")

# Example 5 — “Generative AI” (randomly generated dataset)

# We’ll generate a dataset and actually visualize something from it.

rng = np.random.default_rng(42)  # reproducible

data_ai = {
    "Age": rng.integers(18, 65, size=1000),
    "City": rng.choice(["New York", "London", "Paris", "Tokyo"], size=1000),
    "Industry": rng.choice(["Tech", "Finance", "Retail", "Manufacturing"], size=1000),
    "Income": rng.integers(30_000, 100_000, size=1000)
}
df_ai = pd.DataFrame(data_ai)

# Example visualization 5a: Income histogram
plt.figure()
plt.hist(df_ai["Income"], bins=20)
plt.title("Example 5a: Income Distribution (AI-Generated)")
plt.xlabel("Income")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("example5a_income_hist.png")
plt.close()
print("Saved example5a_income_hist.png")

# Example visualization 5b: Average income by city (bar chart)
avg_income_by_city = df_ai.groupby("City")["Income"].mean()

plt.figure()
plt.bar(avg_income_by_city.index, avg_income_by_city.values)
plt.title("Example 5b: Avg Income by City")
plt.xlabel("City")
plt.ylabel("Average Income")
plt.tight_layout()
plt.savefig("example5b_avg_income_by_city.png")
plt.close()
print("Saved example5b_avg_income_by_city.png")

# What you’ll get

# example1_lists.png

# example2_dict.png

# example3_dataframe.png

# example4_csv.png (and a generated data.csv)

# example5a_income_hist.png

# example5b_avg_income_by_city.png

# Open them in your editor’s file explorer. 
# If you’re in Jupyter instead, you can drop the matplotlib.use("Agg") line and the plt.savefig(...) / plt.close() pairs, and just call plt.show() after each plot (or use %matplotlib inline).