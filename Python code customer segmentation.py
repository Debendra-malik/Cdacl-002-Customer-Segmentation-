import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("shopping_trends.csv")

# Basic EDA
print(df.head())
print(df.describe())

# Encoding categorical columns
encoder = LabelEncoder()
categorical_cols = ['Gender', 'Category', 'Season', 'Payment Method', 'Subscription Status']

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])

# Features for clustering
features = df[['Age', 'Purchase Amount (USD)', 'Previous Purchases',
               'Subscription Status', 'Frequency of Purchases']]

# Scaling
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Cluster analysis
print(df.groupby('Cluster').mean())

# Visualization
plt.figure()
plt.scatter(df['Age'], df['Purchase Amount (USD)'], c=df['Cluster'])
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()
