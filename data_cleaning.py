import pandas as pd
df = pd.read_excel("data_cleaning_pandas.xlsx")
print(df.head())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum().sum())
missing = df.isnull().sum()
print(missing[missing > 0])
print(df.select_dtypes(include="number").columns)
df["Age"] = df["Age"].fillna(df["Age"].mean())

df["Unit_Price"] = df["Unit_Price"].fillna(df["Unit_Price"].mean())

df["Quantity"] = df["Quantity"].fillna(df["Quantity"].mean())

df["Order_ID"]=df["Order_ID"].fillna(df["Order_ID"].mean())

df["Discount"]=df["Discount"].fillna(df["Discount"].mean())

df["Sales"]=df["Sales"].fillna(df["Sales"].mean())

df["Cost"]=df["Cost"].fillna(df["Cost"].mean())

df["Profit"]=df["Profit"].fillna(df["Profit"].mean())

df["Rating"]=df["Rating"].fillna(df["Rating"].mean())

df.ffill(inplace=True)

print(df.isnull().sum())

 
print(df.duplicated())

print(df.duplicated().sum())

duplicates = df[df.duplicated()] 
print(duplicates)


df = df.drop_duplicates()

print(df.duplicated().sum())

print(df.shape)

df = df.drop_duplicates() 
print(df.shape)

print(df.duplicated().sum())

print(df["Order_ID"].duplicated().sum())

duplicates = df[df["Order_ID"].duplicated(keep=False)]
print(duplicates)

df = df.drop_duplicates(subset="Order_ID", keep="first")

print(df["Order_ID"].duplicated().sum())

print(df.columns)

df.columns = df.columns.str.strip()

df.columns = df.columns.str.lower()

df.columns = df.columns.str.replace(" ", "_")


print(df.columns)

string_columns = df.select_dtypes(include="object").columns

for col in string_columns:
    df[col] = df[col].str.strip()

print(df.select_dtypes(include="object").columns)



print(df.dtypes)


df["age"] = pd.to_numeric(df["age"], errors="coerce") 
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce") 
df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce") 
df["discount"] = pd.to_numeric(df["discount"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["cost"] = pd.to_numeric(df["cost"], errors="coerce") 
df["profit"] = pd.to_numeric(df["profit"], errors="coerce")
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")


df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["delivery_date"] = pd.to_datetime(df["delivery_date"], errors="coerce")

print(df.dtypes)

print(df.head())

print(df[df["age"] < 0])

df.loc[df["age"] < 0, "age"] = pd.NA

df["age"] = df["age"].fillna(df["age"].mean())

print(df[df["quantity"] <= 0])

df.loc[df["quantity"] <= 0, "quantity"] = pd.NA

df["quantity"] = df["quantity"].fillna(df["quantity"].median())

print(df[(df["discount"] < 0) | (df["discount"] > 100)])


df.loc[(df["discount"] < 0) | (df["discount"] > 100), "discount"] = 0


print(df["gender"].unique())



df["gender"] = df["gender"].replace({
    "M": "Male",
    "male": "Male",
    "F": "Female",
    "female": "Female",
    "FEMALE": "Female"
})

print(df["payment_method"].unique())


df["payment_method"] = df["payment_method"].replace({ "CARD": "Card", "card": "Card", "upi": "UPI" })

df["returned"] = df["returned"].replace({ "Y": "Yes", "N": "No" })

print(df.head()) 
print(df["gender"].value_counts()) 
print(df["payment_method"].value_counts())
print(df["returned"].value_counts())

print(df[["age", "quantity", "unit_price", "sales", "profit"]].describe())

Q1 = df["sales"].quantile(0.25)
Q3 = df["sales"].quantile(0.75)
IQR = Q3 - Q1 
print("Q1:", Q1)
print("Q3:", Q3) 
print("IQR:", IQR)

lower_limit = Q1 - 1.5 * IQR 
upper_limit = Q3 + 1.5 * IQR 
print("Lower Limit:", lower_limit) 
print("Upper Limit:", upper_limit)


outliers = df[(df["sales"] < lower_limit) | (df["sales"] > upper_limit)]

print(outliers)

print(outliers.shape)


df = df[(df["sales"] >= lower_limit) & (df["sales"] <= upper_limit)]


print(df.shape)

new_outliers = df[(df["sales"] < lower_limit) | (df["sales"] > upper_limit)]

print(new_outliers.shape)

df["profit_margin"] = (df["profit"] / df["sales"]) * 100

df["sales_after_discount"] = df["sales"] - (df["sales"] * df["discount"] / 100)

df["calculated_cost"] = df["sales"] - df["profit"]

df["delivery_days"] = (df["delivery_date"] - df["order_date"]).dt.days

df["age_group"] = pd.cut(df["age"], bins=[0, 18, 30, 45, 60, 100], labels=["Teen", "Young", "Adult", "Middle Age", "Senior"])

print(df[["profit_margin", "sales_after_discount", "delivery_days", "age_group"]].head())

print(df[["order_date", "delivery_date"]].dtypes)

df["order_year"] = df["order_date"].dt.year

df["order_month"] = df["order_date"].dt.month

df["month_name"] = df["order_date"].dt.month_name()

df["order_day"] = df["order_date"].dt.day

df["day_name"] = df["order_date"].dt.day_name()

df["quarter"] = df["order_date"].dt.quarter

df["week_number"] = df["order_date"].dt.isocalendar().week

print(df[[ "order_date", "order_year", "order_month", "month_name", "order_day", "day_name", "quarter", "week_number" ]].head())

df["customer_name"] = df["customer_name"].str.lower()
df["city"] = df["city"].str.lower()

df["state"] = df["state"].str.upper()

df["customer_name"] = df["customer_name"].str.title() 
df["city"] = df["city"].str.title()

df["payment_method"] = df["payment_method"].str.replace("Card", "Credit Card")

print(df["email"].str.contains("@", na=False))

print(df["customer_name"].str.startswith("A", na=False))

print(df["product_name"].str.endswith("e", na=False))

df[["username", "domain"]] = df["email"].str.split("@", expand=True)

df["name_length"] = df["customer_name"].str.len()

print(df[[ "customer_name", "email", "username", "domain", "name_length" ]].head())

df.sort_values(by="sales", inplace=True) 
print(df[["order_id", "sales"]].head())

df.sort_values(by="sales", ascending=False, inplace=True)

print(df[["order_id", "sales"]].head())


df.sort_values( by=["city", "sales"], ascending=[True, False], inplace=True ) 
print(df[["city", "sales"]].head())

high_sales = df[df["sales"] > 5000] 
print(high_sales.head())

mumbai_data = df[df["city"] == "Mumbai"]
print(mumbai_data.head())

result = df[ (df["sales"] > 5000) & (df["payment_method"] == "Card") ]
print(result.head())

result = df.query("sales > 5000")

print(result.head())

result = df.query("sales > 5000 and quantity >= 2")

print(result.head())

print(df[[ "customer_name", "city", "sales" ]].head())

df.reset_index(drop=True, inplace=True) 
print(df.head())

print(df.shape)
print(df.head())

city_sales = df.groupby("city")["sales"].sum() 
print(city_sales)

category_sales = df.groupby("product_category")["sales"].mean() 
print(category_sales)

payment_count = df.groupby("payment_method")["order_id"].count() 
print(payment_count)


summary = df.groupby("city")["sales"].agg([ "sum", "mean", "max", "min", "count" ]) 
print(summary)

city_category = df.groupby( ["city", "product_category"] )["sales"].sum()
print(city_category)

sales_rep_profit = df.groupby("sales_rep")["profit"].sum() 
print(sales_rep_profit)

rating = df.groupby("product_category")["rating"].mean() 
print(rating)


top_cities = ( df.groupby("city")["sales"] .sum() .sort_values(ascending=False) .head(5) )
print(top_cities)

report = df.groupby("city").agg({ "sales": "sum", "profit": "sum", "quantity": "sum", "rating": "mean" })
print(report)

report = report.reset_index() 
print(report.head())

print(df.shape)

print(df.dtypes)

print(df.isnull().sum())

print(df.duplicated().sum())

print(df["order_id"].duplicated().sum())

print(df["gender"].unique()) 
print(df["payment_method"].unique()) 
print(df["returned"].unique())

print(df.describe())

print(df[df["age"] < 0])
print(df[df["quantity"] <= 0]) 
print(df[df["discount"] > 100])

print(df.info())

gender_mapping = {
    "Aditya": "Male",
    "Rahul": "Male",
    "Amit": "Male",
    "Priya": "Female",
    "Sneha": "Female",
    "Neha": "Female"
}

df["gender"] = df["customer_name"].map(gender_mapping)



print(df[["customer_name", "gender"]].head(10))

df["sales"] = df["quantity"] * df["unit_price"]

print(df.head())
print(df.tail())
print("Total Sales:", df["sales"].sum())
print("Total Profit:", df["profit"].sum())
print("Average Sales:", df["sales"].mean())


top_cities = ( df.groupby("city")["sales"] .sum() .sort_values(ascending=False) .head(5) ) 
print(top_cities)

best_category = ( df.groupby("product_category")["sales"] .sum() .sort_values(ascending=False) )
print(best_category)

print(df["payment_method"].value_counts())

print(df.groupby("region")["sales"].sum())

monthly_sales = ( df.groupby("month_name")["sales"] .sum() ) 
print(monthly_sales)

top_sales_rep = ( df.groupby("sales_rep")["profit"] .sum() .sort_values(ascending=False) .head(5) ) 
print(top_sales_rep)

print("Average Rating:", df["rating"].mean())

print(df["returned"].value_counts())

summary = { "Total Sales": df["sales"].sum(), "Total Profit": df["profit"].sum(), "Average Sales": df["sales"].mean(), "Average Rating": df["rating"].mean() } 
print(summary)

print(df["sales"].sum())


print(df[["quantity", "unit_price", "sales"]].head(20))


df.to_csv("sales_data_cleaned.csv", index=False)

df.to_excel("sales_data_cleaned.xlsx", index=False)

df.to_csv(r"D:\Sales_Data_Cleaning_Project\sales_data_cleaned.csv", index=False)
df.to_excel(r"D:\Sales_Data_Cleaning_Project\sales_data_cleaned.xlsx", index=False)


 