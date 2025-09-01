import pandas as pd

# Load the dataset into a pandas DataFrame
df = pd.read_csv(r"C:\Users\SCSM11\Documents\Kaggle Dataset\customer-segmentation-ecommerce\online_retail.csv")

# Display the first few rows of the dataset
print(df.head())

# Initial data exploration
print(df.head())
print(df.info())
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# Show Rows with Nulls in a Specific Column
df[df['Description'].isnull()]

# Drop rows where InvoiceID is missing
df = df.dropna(subset=['InvoiceNo'])

# Fill missing Description with those from other rows with the same StockCode
# Classic group-based fill
# df['Description'] = df.groupby('StockCode')['Description'].transform(lambda x: x.fillna(method='ffill'))
# df['Description'] = df.groupby('StockCode')['Description'].transform(lambda x: x.fillna(method='bfill'))
df['Description'] = df.groupby('StockCode')['Description'].transform(lambda x: x.fillna(method='ffill').fillna(method='bfill'))

# If datetime format is not consistent
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'],errors="coerce") 

# Check for duplicates
df.duplicated().sum()

# Remove outliers
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Remove cancellations (Negative Invoices)
df = df[~df['InvoiceNo'].astype(str).str.startswith('C')] # Cancel invoice with invoice numbers starting with 'C'

# Create a total price column
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print("Unique Stock Code:",df['StockCode'].nunique())
print("Unique Description:",df['Description'].nunique())
print("Unique Customer ID:",df['CustomerID'].nunique())
print("Unique Country:",df['Country'].nunique()) 

# Show which StockCode have more than one Description
df.groupby('StockCode')['Description'].nunique().sort_values(ascending=False).head(10)

# Align using the most frequent description
mode_desc = (
    df.dropna(subset=['Description'])   # ignore NaNs
      .groupby('StockCode')['Description']
      .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
)

# Keep original description for reference
df['Description_original'] = df['Description']

# Replaces all Description values — missing or conflicting ones
df['Description'] = df['StockCode'].map(mode_desc)

# Save the cleaned data back to excel
df.to_excel('filtered_data_online_retail.csv', index=False)

############ EDA ##############
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'],errors="coerce")
df['Month'] = df['InvoiceDate'].dt.to_period('M')
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

# Plot sales by month
import matplotlib.pyplot as plt
monthly_sales.plot(kind='line', figsize=(12,6), title='Monthly Revenue')
plt.ylabel("Revenue")
plt.show()

# Top 10 products by revenue
top_products_by_revenue = df.groupby('Description')['TotalPrice'].sum().sort_values(ascending=False).head(10)
top_products_by_revenue.plot(kind='barh',figsize=(10,6),title='Top 10 Products by Revenue')

# Top 10 products by quantity sold
top_products_by_quantity = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
top_products_by_quantity.plot(kind='barh',figsize=(10,6),title='Top 8 Products by Quantity')

plt.savefig("TopProductByQuantity.png")
plt.show()

# Top 10 best selling countries
top_sales_country = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False).head(10)
top_sales_country.plot(kind='bar',figsize=(10,6),title='Top 10 Best Selling Country',xlabel='Total Sales')

plt.savefig("TopSalesCountry.png")
plt.show()

# Top customers sales by revenue
top_customers = df.groupby('CustomerID')['TotalPrice'].sum().sort_values(ascending=False).head(10)
top_customers.plot(kind="bar",figsize=(12,6),title='Top Customers')

plt.ylabel("Total Sales")
plt.title("Sales per customer")
plt.show()

# To show the top 20 Customer Order Frequency
order_freq = df.groupby('CustomerID')['InvoiceNo'].nunique().sort_values(ascending=False).head(20)
order_freq.plot(kind='bar',figsize=(12,6),title="Distribution Customer Order Frequency",ylabel="Number of Orders")
plt.show()