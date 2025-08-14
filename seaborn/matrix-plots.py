"""
Matrix plots
------------
There are two ways to visualize matrix plots with Seaborn. 
Matrix plots, also known as heatmaps or correlation matrices, are a type of data visualization that represents the values in a 2D matrix using color-coded cells. 
These plots are particularly useful for visualizing and understanding the relationships among multiple variables in a dataset.

Heatmap:
A heatmap visualizes a matrix of values as a color-coded grid, as shown in the following code snippet.
    corr_matrix = tips.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="Y10Rd")

This example heatmap provides a clear visual representation of the relationships among features in the Iris flower dataset, which can be useful for understanding the underlying patterns and structure of the data. 

Clustermap:
A clustermap visualizes a correlation matrix with hierarchical clustering, as shown in the following code snippet.
    sns.clustermap(corr_matrix, cmap="Y10Rd")

This example clustermap performs hierarchical clustering on the data and displays the results in a heatmap format, along with dendrograms on the side to show the clustering relationships in the Iris flower dataset.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# Load your data
# ==============================
# Option 1: Built-in Iris dataset (ready to run)
iris = sns.load_dataset("iris")

# Option 2: Your CSV (uncomment to use)
# iris = pd.read_csv("my_iris_like_data.csv")
# Your CSV should have numeric feature columns similar to:
#   sepal_length,sepal_width,petal_length,petal_width,species
# If your headers differ, rename them before plotting:
# iris = iris.rename(columns={
#     "SepalLength":"sepal_length",
#     "SepalWidth":"sepal_width",
#     "PetalLength":"petal_length",
#     "PetalWidth":"petal_width"
# })

# Numeric columns only for correlations
num_cols = iris.select_dtypes(include="number")

# ==============================
# 1) Heatmap of the correlation matrix
# ==============================
corr_matrix = num_cols.corr()  # Pandas 2.x uses numeric-only by default on numeric slice

plt.figure(figsize=(8, 6))
# NOTE: The colormap in the text "Y10Rd" is a typo; the valid name is "YlOrRd".
sns.heatmap(corr_matrix, annot=True, cmap="YlOrRd", vmin=-1, vmax=1, square=True)
plt.title("Correlation Heatmap of Iris Dataset")
plt.tight_layout()
plt.savefig("iris_correlation_heatmap.png")
plt.show()

# ==============================
# 2) Clustermap (hierarchical clustering heatmap)
# ==============================
# You can cluster the *correlation matrix* (4x4), or the *standardized data* (150x4).
# The screenshot-like look usually comes from clustering the standardized data.
# We'll do standardized data for a richer clustermap:
g = sns.clustermap(
    num_cols,                 # raw numeric features (150 x 4)
    cmap="YlOrRd",            # same family as above
    standard_scale=1,         # standardize each column (makes colors comparable)
    figsize=(9, 9)
)
g.fig.suptitle("Clustered Heatmap of Iris Dataset", fontsize=14)
g.fig.subplots_adjust(top=0.95)  # ensure the title isn't clipped
g.savefig("iris_clustermap.png")
plt.show()

# ---- Alternative: clustermap of the correlation matrix (uncomment if you prefer 4x4) ----
g_corr = sns.clustermap(corr_matrix, cmap="YlOrRd", figsize=(6, 6))
g_corr.fig.suptitle("Clustered Correlation Matrix (Iris)", fontsize=14)
g_corr.fig.subplots_adjust(top=0.93)
g_corr.savefig("iris_clustermap_corr.png")
plt.show()

# The Iris dataset is the “hello world” of classical machine-learning. 
# It’s a tiny, clean table of 150 flower samples with 4 numeric measurements and a species label.

# What’s in it
# Rows: 150 (balanced: 50 per species)
# Species (label): setosa, versicolor, virginica

# Features (all in centimeters):
# sepal_length
# sepal_width
# petal_length
# petal_width

# Where it came from
# Measurements were collected by botanist Edgar Anderson.
# Popularized in R. A. Fisher’s 1936 paper on linear discriminant analysis. That’s why you’ll also hear it called Fisher’s Iris.

# Why everyone uses it
# It’s small and balanced → great for demos.
# The structure is tabular and numeric → no preprocessing drama.

# It shows real patterns:
# setosa is trivially separable by petal length/width (tiny petals).
# versicolor vs virginica overlap a bit → good for illustrating model tradeoffs.

# How to load it (Seaborn)
# import seaborn as sns
# iris = sns.load_dataset("iris")   # 150 x 5 DataFrame

# Typical uses
# Quick visualizations: pairplots, heatmaps, clustermaps.
# Teaching classification: k-NN, logistic regression, SVM, LDA.
# Explaining metrics: confusion matrices, ROC curves.