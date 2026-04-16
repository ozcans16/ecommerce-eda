
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


os.makedirs("images", exist_ok=True)


df = pd.read_csv("data/online_retail.csv", encoding="ISO-8859-1")


df = df.dropna()
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]


df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]


top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 10 Products")
plt.xticks(rotation=45)
plt.savefig("images/top_products.png", bbox_inches="tight")
plt.close()


top_customers = df.groupby("CustomerID")["TotalPrice"].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=top_customers.values, y=top_customers.index)
plt.title("Top Customers")
plt.savefig("images/top_customers.png", bbox_inches="tight")
plt.close()


df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Hour"] = df["InvoiceDate"].dt.hour

hourly_sales = df.groupby("Hour")["TotalPrice"].sum()

plt.figure()
sns.lineplot(x=hourly_sales.index, y=hourly_sales.values)
plt.title("Sales by Hour")
plt.savefig("images/hourly_sales.png", bbox_inches="tight")
plt.close()


country_sales = df.groupby("Country")["TotalPrice"].sum().sort_values(ascending=False).head(10)

plt.figure()
sns.barplot(x=country_sales.values, y=country_sales.index)
plt.title("Sales by Country")
plt.savefig("images/country_sales.png", bbox_inches="tight")
plt.close()


basket = df.groupby(["InvoiceNo", "Description"])["Quantity"].sum().unstack().fillna(0)
basket = basket.applymap(lambda x: 1 if x > 0 else 0)

corr = basket.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr)
plt.title("Product Correlation")
plt.savefig("images/correlation.png", bbox_inches="tight")
plt.close()


basket_value = df.groupby("InvoiceNo")["TotalPrice"].sum()

plt.figure()
sns.histplot(basket_value, bins=50)
plt.title("Basket Value Distribution")
plt.savefig("images/basket_value.png", bbox_inches="tight")
plt.close()

print(" Tüm analizler tamamlandı, grafikler images/ klasörüne kaydedildi.")