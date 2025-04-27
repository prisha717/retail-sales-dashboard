import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('superstore.csv')

total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = df['Sales'].mean()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${avg_order_value:,.2f}")

df['Order Date'] = pd.to_datetime(df['Order Date'])
sales_over_time = df.groupby('Order Date')['Sales'].sum()
sales_over_time.plot(figsize=(12,6))
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
top_products.plot(kind='bar', figsize=(12,6))
plt.title('Top 10 Products by Sales')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.show()

# Plot: Sales by Region
sales_by_region = df.groupby('Region')['Sales'].sum()
sales_by_region.plot(kind='pie', autopct='%1.1f%%', figsize=(8,8))
plt.title('Sales by Region')
plt.ylabel('')
plt.show()