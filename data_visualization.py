import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("SampleSuperstore.csv")

# Display first 5 rows
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nShape of Dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nSummary Statistics:")
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,5))
sns.countplot(x="Category", data=df)
plt.title("Number of Orders by Category")
plt.savefig("category_count.png")
plt.show()

plt.figure(figsize=(8,5))
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.savefig("sales_by_category.png")
plt.show()


plt.figure(figsize=(8,5))
df.groupby("Region")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.savefig("sales_by_region.png")
plt.show()


plt.figure(figsize=(7,7))
df.groupby("Category")["Profit"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Profit by Category")
plt.ylabel("")
plt.savefig("profit_by_category.png")
plt.show()


plt.figure(figsize=(8,5))
sns.scatterplot(x="Sales", y="Profit", data=df)
plt.title("Sales vs Profit")
plt.savefig("sales_vs_profit.png")
plt.show()


plt.figure(figsize=(8,5))
sns.boxplot(x=df["Sales"])
plt.title("Sales Box Plot")
plt.savefig("sales_boxplot.png")
plt.show()


plt.figure(figsize=(8,6))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()