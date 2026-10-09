# ============================================================
# Seaborn Library in Python
# Assignment: Space Mission Data Explorer
# ============================================================

import seaborn as sns
import matplotlib.pyplot as plt

# ---- PART 1: Import and Load Data ----
# Load Seaborn's built-in planets dataset and remove missing values
df = sns.load_dataset('planets')
df = df.dropna()

print("First 5 rows:")
print(df.head())
print()

print("Dataset Info:")
print(df.info())
print()

print("Summary Statistics:")
print(df.describe())
print()

print("Discovery Methods:")
print(df['method'].unique())
print()

# ---- PART 2: Histogram ----
# Distribution of Planet Orbital Periods
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='orbital_period', bins=20, color='steelblue')
plt.title('Distribution of Planet Orbital Periods')
plt.xlabel('Orbital Period (Days)')
plt.ylabel('Count')
plt.show()

# ---- PART 3: KDE Plot and Fitting Distribution ----
# Distance Pattern (KDE plot only)
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x='distance', fill=True)
plt.title('Distance Pattern of Planet Discoveries (KDE)')
plt.xlabel('Distance (Parsecs)')
plt.show()

# Distance Pattern (Histogram with fitted KDE curve)
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='distance', kde=True, color='coral')
plt.title('Planet Distance — Histogram with KDE Curve')
plt.xlabel('Distance (Parsecs)')
plt.ylabel('Count')
plt.show()

# ---- PART 4: Scatter Plot ----
# Comparing Distance vs Orbital Period by Discovery Method
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x='distance', y='orbital_period', hue='method')
plt.title('Distance vs Orbital Period by Discovery Method')
plt.xlabel('Distance (Parsecs)')
plt.ylabel('Orbital Period (Days)')
plt.show()

# ---- PART 5: Heatmap ----
# Correlation matrix across numerical features
corr = df.corr(numeric_only=True)
print("Correlation table:")
print(corr)
print()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap — Planet Discovery Data')
plt.show()