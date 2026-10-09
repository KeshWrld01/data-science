# ============================================================
# Module 14: Capstone Project — IMDB Movie Dataset Analysis
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------------------------------------
# 1. Import the dataset using Pandas
# ------------------------------------------------------------
# Load the dataset (replace 'imdb_movies.csv' with your local filename/path)
df = pd.read_csv('imdb_movies.csv')

# ------------------------------------------------------------
# 2. Print the first three and last three rows of the dataset
# ------------------------------------------------------------
print("=== First 3 Rows ===")
print(df.head(3))
print("\n=== Last 3 Rows ===")
print(df.tail(3))

# ------------------------------------------------------------
# 3. Check the detailed information of the dataset
# ------------------------------------------------------------
print("\n=== Dataset Information ===")
df.info()

print("\n=== Dataset Shape (Rows, Columns) ===")
print(df.shape)

# ------------------------------------------------------------
# 4. Check if any null values are present or not in the dataset
# ------------------------------------------------------------
print("\n=== Missing Values Count per Column ===")
print(df.isnull().sum())

# ------------------------------------------------------------
# 5. Create a subset of the original dataset with data of row number between 41 to 75
# ------------------------------------------------------------
# Using iloc slicing for row positions 41 through 75 (inclusive)
subset_df = df.iloc[41:76]
print("\n=== Subset (Rows 41 to 75) ===")
print(subset_df.head())

# ------------------------------------------------------------
# 6. Check details of the movie that has the highest number of votes
# ------------------------------------------------------------
# Locates the row where 'No_of_Votes' is at its maximum
max_votes_movie = df.loc[df['No_of_Votes'].idxmax()]
print("\n=== Movie with Highest Number of Votes ===")
print(max_votes_movie)

# ------------------------------------------------------------
# 7. Create boxplot for features - IMDB_Rating and Runtime
# ------------------------------------------------------------
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.boxplot(y=df['IMDB_Rating'], color='skyblue')
plt.title('Boxplot of IMDB Rating')

plt.subplot(1, 2, 2)
sns.boxplot(y=df['Runtime'], color='lightgreen')
plt.title('Boxplot of Runtime (Minutes)')

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 8. Check the relationship between features IMDB_Rating and Runtime using Matplotlib
# ------------------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df['Runtime'], df['IMDB_Rating'], color='purple', alpha=0.6, edgecolors='w')
plt.title('Relationship between Runtime and IMDB Rating')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('IMDB Rating')
plt.grid(True)
plt.show()

# ------------------------------------------------------------
# 9. Check the distribution of features IMDB_Rating and Runtime
# ------------------------------------------------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df['IMDB_Rating'], kde=True, color='teal', bins=15)
plt.title('Distribution of IMDB Rating')

plt.subplot(1, 2, 2)
sns.histplot(df['Runtime'], kde=True, color='coral', bins=15)
plt.title('Distribution of Runtime')

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 10. Create a count plot of feature Rating to display no. of movies with a particular rating
# ------------------------------------------------------------
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='Certificate', palette='viridis')  # Certificate/Rating column
plt.title('Number of Movies per Rating / Certificate Category')
plt.xlabel('Rating Certificate')
plt.ylabel('Movie Count')
plt.xticks(rotation=45)
plt.show()