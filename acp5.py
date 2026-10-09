# ============================================================
# Advanced Visualizations in Python
# Assignment: Restaurant Customer Insights Explorer
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ---- PART 1: Bar Plot and Count Plot ----
# Load Seaborn's built-in tips dataset and drop missing values
df = sns.load_dataset('tips')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()

print("Dataset Info:")
print(df.info())
print()

# Bar Plot — Average bill per day by gender
sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Customer Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

# Count Plot — Number of customers per day by gender
sns.countplot(x='day', hue='sex', data=df)
plt.title('Number of Customers per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

# ---- PART 2: Box Plot, Strip Plot and Swarm Plot ----
# Box Plot — Spread of bills per day
sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Spread of Customer Bills per Day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

# Strip Plot — Every bill amount per day
sns.stripplot(x='day', y='total_bill', data=df, jitter=True)
plt.title('Every Customer Bill per Day (Strip Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

# Swarm Plot — Every dot arranged without overlap
sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Every Customer Bill per Day (Swarm Plot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

# ---- PART 3: Joint Plots ----
# Standard Joint Plot — Scatter with edge histograms
sns.jointplot(x='total_bill', y='tip', data=df)
plt.suptitle('Customer Bill vs Tip', y=1.02)
plt.show()

# KDE Joint Plot — Density distribution map
sns.jointplot(x='total_bill', y='tip', data=df, kind='kde')
plt.suptitle('Customer Bill vs Tip - KDE Joint Plot', y=1.02)
plt.show()

# ---- PART 4: Pair Plot ----
# Pairwise relationships across numeric columns
sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair Plot - Bill, Tip and Party Size', y=1.02)
plt.show()

# ---- PART 5: Point Plot and lmplot ----
# Point Plot — Trend of averages with confidence intervals
sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Customer Bill per Day by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

# lmplot — Scatter plot with linear regression trend line
sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Customer Bill vs Tip - Trend Line')
plt.show()