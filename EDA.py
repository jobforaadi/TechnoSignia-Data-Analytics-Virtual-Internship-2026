import pandas as pd
df = pd.read_excel("sales_data_cleaned.xlsx")

# Dataset Overview
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.isnull().sum())
print(df.shape)
print(df.info())
print(df.describe())

print(df.describe(include="all"))

print(df["city"].value_counts())
print(df["product_category"].value_counts())
print(df["payment_method"].value_counts())

print("Total Sales:", df["sales"].sum())
print("Average Sales:", df["sales"].mean())
print("Maximum Sales:", df["sales"].max())
print("Minimum Sales:", df["sales"].min())

print("Total Profit:", df["profit"].sum())
print("Average Profit:", df["profit"].mean())


print(df.groupby("city")["sales"].sum())
print(df.groupby("product_category")["sales"].sum())
print(df.groupby("payment_method")["sales"].sum())


print(df.corr(numeric_only=True))

print(df.nlargest(10, "sales"))
print(df.nsmallest(10, "sales"))