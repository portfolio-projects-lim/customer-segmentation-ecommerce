🛒 Customer Segmentation for E-commerce Business


📌 Project Overview

This project analyzes an online retail dataset to identify key customer segments using RFM (Recency, Frequency, Monetary) analysis. The goal is to help the business understand customer behavior, identify high-value customers, and support data-driven marketing strategies.


📌 Dataset

Online Retail Dataset (Kaggle)

~540,000 transactions (2010 - 2011)

InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country


📌 Skills & Tools

Python: pandas, matplotlib, seaborn, mlxtend

SQL: SQLite for data queries

Tableau: Interactive dashboards for visualization

Excel: Data cleaning and quick analysis


🪜 Project Steps

1️⃣ Data Cleaning

Removed duplicates, negative quantities, missing InvoiceNo, cancellation (if any).

Filled missing Description with those rows with the same StockCode.

Checked for Description consistency (Align StockCode which have more than one Description).

Created new column, TotalPrice = Quantity * UnitPrice.

📈 Raw Downloaded Excel file: online_retail.csv

📈 Cleaned Excel file: filtered_data_online_retail.csv


2️⃣ Exploratory Data Analysis (EDA)

Revenue by month, top-selling products, country-wise sales distribution, customer behavior and spending distribution.

📝 customers_segmentation_ecommerce.py


3️⃣ Customer Segmentation

RFM Analysis - Calculated Recency, Frequency, Monetary value for each customer.

Assign RFM Scores - 1 to 5 using quantiles.

Define customer segments - Champions, Loyal, Potential Loyalists, At Risk, Lost.

Deep Dive Analysis on Champions: Purchasing Trends, Top Products, Seasonal Patterns.

Basket Analysis (frequent product combinations).

📈 RFM_Segmentation.csv

📈 basket_rules_compute.csv


4️⃣ Visualization (Tableau)

KPIs: Total Revenue, Total Customers, AOV, Repeat Rate.

Segmentation Distribution.

Revenue Contribution by Segment.

Monthly Trend Analysis.

Product Insights.

Basket Analysis.

📊 Customer Segmentation & Insights.twbx

I've published my Tableau workbook. You can view the interactive dashboard here:

[View Tableau Dashboard](https://public.tableau.com/views/CustomerSegmentationInsights_17564342118620/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

