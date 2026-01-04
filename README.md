## Cdacl-002-Customer-Segmentation-
This project analyzes U.S. retail customer purchase data to segment customers based on age, spending behavior, season, location, and card usage. SQL and Python were used for data analysis, and clustering techniques grouped customers into segments to identify trends, optimize discounts, and create targeted marketing strategies for business growth..

# 1..........
## TITLE
Customer Segmentation Analysis
CDACL-002
Name: Debendra Malik
Role: Data Analyst

## Business Problem
Businesses want to understand customer shopping behavior
Identify where discounts should be applied
Segment customers for targeted marketing

## Dataset Overview
3,900 customer purchase records
U.S. market shopping data
Includes age, category, season, payment method, discounts

## Project Objectives
Identify discount-worthy product categories
Analyze card spending by age, season, and location
Perform customer clustering
Recommend marketing strategies

## Data Preprocessing
Removed duplicates
Handled missing values
Encoded categorical variables
Normalized numerical data

## Discount Analysis
Best Categories for Discounts
Clothing
Accessories
Footwear
Reason
High purchase frequency
Customers respond strongly to discounts

## Age-Based Card Spending
18–25: Low spend, high discount usage
26–35: Highest card spending
36–50: Stable spending
50+: High value, low frequency

## Season & Location Impact
Winter: Clothing & footwear sales high
Festive season: Maximum spending
Urban customers: More card usage

## Clustering Approach
Algorithm: K-Means
Number of clusters: 4
Key features: Age, Spend, Frequency, Discount usage

## Cluster 1 – Price Sensitive
Young customers
Low spending
High discount usage
Strategy: Flash sales, student offers

## Cluster 2 – Loyal High Spenders
Age 26–40
Subscription users
High repeat purchases
Strategy: Loyalty rewards, premium offers
Slide 12: Cluster 3 – Seasonal Buyers
Purchase during festivals
Moderate spending
Strategy: Festival campaigns

## Cluster 4 – Premium Customers
Age 40+
High value per order
Strategy: Personalized offers

## Conclusion
Segmentation improves marketing efficiency
Discounts should be category and age specific
Personalized campaigns increase revenue

# 2.......
# SQL QUERIES USED FOR ANALYSIS (MySQL)
## -- Total customers
SELECT COUNT(DISTINCT customer_id) FROM shopping_trends;

## -- Category-wise total sales
SELECT category, SUM(`purchase amount (usd)`) AS total_sales
FROM shopping_trends
GROUP BY category
ORDER BY total_sales DESC;

## -- Discount impact by category
SELECT category,
COUNT(*) AS total_orders,
SUM(CASE WHEN `discount applied` = 'Yes' THEN 1 ELSE 0 END) AS discount_orders
FROM shopping_trends
GROUP BY category;

## -- Age-wise average spending
SELECT age, AVG(`purchase amount (usd)`) AS avg_spend
FROM shopping_trends
GROUP BY age
ORDER BY age;

## -- Season-wise sales
SELECT season, SUM(`purchase amount (usd)`) AS season_sales
FROM shopping_trends
GROUP BY season;

## -- Payment method usage
SELECT `payment method`, COUNT(*) AS usage_count
FROM shopping_trends
GROUP BY `payment method`;

## -- Location-wise spending
SELECT location, AVG(`purchase amount (usd)`) AS avg_spend
FROM shopping_trends
GROUP BY location;

# 3 ............
## PYTHON CODE (EDA + CLUSTERING)
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

## Load data
df = pd.read_csv("shopping_trends.csv")

## Basic EDA
print(df.head())
print(df.describe())

## Encoding categorical columns
encoder = LabelEncoder()
categorical_cols = ['Gender', 'Category', 'Season', 'Payment Method', 'Subscription Status']

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

## Features for clustering
features = df[['Age', 'Purchase Amount (USD)', 'Previous Purchases',
               'Subscription Status', 'Frequency of Purchases']]

## Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

## KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

## Cluster analysis
print(df.groupby('Cluster').mean())

## Visualization
plt.figure()
plt.scatter(df['Age'], df['Purchase Amount (USD)'], c=df['Cluster'])
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()

# 4......
# POWER BI DASHBOARD – CUSTOMER SEGMENTATION


# 5 ................
# PROJECT EXPLANATION SCRIPT

“Hello, my name is Debendra Malik.
This project is Customer Segmentation Analysis using U.S. shopping data.
The main goal of this project is to understand customer behavior and improve marketing strategies.
First, I analyzed product categories to find where discounts are most effective. I found that clothing, accessories, and footwear perform better when discounts are applied.
Next, I analyzed card spending based on age, season, and location. Customers between 26 to 35 years spend the most using cards. Spending increases during winter and festive seasons.
Then, I used K-Means clustering to divide customers into four groups based on age, purchase amount, frequency, and discount usage.
Each cluster represents a different customer type, such as price-sensitive, loyal customers, seasonal buyers, and premium shoppers.
Finally, I created targeted marketing strategies for each cluster to increase sales and customer retention.
This project helps businesses take data-driven decisions and improve customer satisfaction. Thank you.”
