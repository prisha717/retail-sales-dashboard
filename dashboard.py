import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('superstore.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Streamlit app
st.title("Retail Sales Dashboard")

# KPIs
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = df['Order ID'].nunique()
avg_order_value = df['Sales'].mean()

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")
st.metric("Total Orders", total_orders)
st.metric("Avg Order Value", f"${avg_order_value:,.2f}")

# Filters
st.sidebar.header("Filters")
region = st.sidebar.selectbox("Select Region", df['Region'].unique())

filtered_df = df[df['Region'] == region]

# Sales over time
st.subheader(f"Sales Over Time in {region}")
sales_over_time = filtered_df.groupby('Order Date')['Sales'].sum()

fig, ax = plt.subplots()
sales_over_time.plot(ax=ax)
st.pyplot(fig)

# Top products
st.subheader(f"Top 5 Products in {region}")
top_products = filtered_df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

fig2, ax2 = plt.subplots()
top_products.plot(kind='bar', ax=ax2)
st.pyplot(fig2)
