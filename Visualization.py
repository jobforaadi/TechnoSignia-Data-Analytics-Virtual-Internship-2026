import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sales_data_cleaned.xlsx")

city_sales = df.groupby("city")["sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
plt.bar(city_sales.index, city_sales.values)
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()



category_sales = df.groupby("product_category")["sales"].sum()

plt.figure(figsize=(8,5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()