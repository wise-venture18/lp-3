#•	ML-4: Implement K-Means or hierarchical clustering on the sales_data_sample.csv dataset. Determine the number of clusters using the elbow method. 
	Dataset link: https://drive.google.com/file/d/1IqYi6yxoJtjlbgt-2K0nEty4c-5cg8-f/view?usp=sharing OR https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print("Dataset Loaded Successfully")
print(data.head())

print("\nDataset Shape:", data.shape)


# =====================================================
# CELL 3: SELECT FEATURES
# =====================================================

# Select numerical sales-related columns
X = data[[
    "SALES",
    "QUANTITYORDERED",
    "PRICEEACH",
    "MSRP"
]]

print("\nSelected Features:")
print(X.head())


# =====================================================
# CELL 4: NORMALIZE DATA
# =====================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nData Normalized Successfully")


# =====================================================
# CELL 5: ELBOW METHOD
# =====================================================

wcss = []

# Calculate WCSS for different cluster values
for i in range(1, 11):

    kmeans = KMeans(
        n_clusters=i,
        random_state=42,
        n_init=10
    )

    kmeans.fit(X_scaled)

    wcss.append(kmeans.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker="o")

plt.title("Elbow Method")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("WCSS")

plt.show()


# =====================================================
# CELL 6: APPLY K-MEANS CLUSTERING
# =====================================================

# Select optimal number of clusters
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
kmeans.fit(X_scaled)

# Assign cluster labels
data["Cluster"] = kmeans.labels_

print("\nClustering Completed Successfully")


# =====================================================
# CELL 7: DISPLAY CLUSTER RESULTS
# =====================================================

print("\nCluster Assignments:")
print(data[["SALES", "QUANTITYORDERED", "Cluster"]].head(10))

print("\nNumber of Records in Each Cluster:")
print(data["Cluster"].value_counts())


# =====================================================
# CELL 8: VISUALIZE CLUSTERS
# =====================================================

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=kmeans.labels_
)

plt.title("K-Means Clustering of Sales Data")
plt.xlabel("Sales (Normalized)")
plt.ylabel("Quantity Ordered (Normalized)")

plt.show()
