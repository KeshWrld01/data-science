# ================================
# SEABORN LIBRARY IN PYTHON
# ACP - CUSTOMER SURVEY DATASET ANALYSER
# ================================

# PART 1 - IMPORT LIBRARIES
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# PART 2 - CREATE THE CUSTOMER SURVEY DATASET
data = {
    'Age': [22, 25, 47, 52, 46, 56, 55, 60, 23, 27],
    'Annual_Income_k': [15, 16, 50, 60, 58, 65, 70, 80, 18, 20],
    'Spending_Score': [39, 81, 6, 77, 40, 76, 94, 3, 72, 79],
    'Gender': ['Male', 'Female', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

# PART 3 - SCATTER PLOT
# Relationship between Annual Income and Spending Score, grouped by Gender
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Annual_Income_k', y='Spending_Score', hue='Gender', s=100)
plt.title('Annual Income vs Spending Score by Gender')
plt.xlabel('Annual Income ($k)')
plt.ylabel('Spending Score (1-100)')
plt.grid(True)
plt.show()

# PART 4 - HISTOGRAM WITH KDE
# Distribution of Customer Ages
plt.figure(figsize=(8, 5))
sns.histplot(df['Age'], kde=True, color='purple', bins=5)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# PART 5 - BOX PLOT
# Comparing Spending Score distribution between Genders
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Gender', y='Spending_Score', palette='Set2')
plt.title('Spending Score Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Spending Score (1-100)')
plt.show()

# PART 6 - BAR PLOT
# Average Annual Income by Gender
plt.figure(figsize=(8, 5))
sns.barplot(data=df, x='Gender', y='Annual_Income_k', palette='Blues_d')
plt.title('Average Annual Income by Gender')
plt.xlabel('Gender')
plt.ylabel('Average Annual Income ($k)')
plt.show()