#•	ML-4: Implement K-Means or hierarchical clustering on the sales_data_sample.csv dataset. Determine the number of clusters using the elbow method. 
	Dataset link: https://drive.google.com/file/d/1IqYi6yxoJtjlbgt-2K0nEty4c-5cg8-f/view?usp=sharing OR https://www.kaggle.com/datasets/kyanyoga/sample-sales-data

# K-Means :=>
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
#===== END OF PROGRAM=======



# OR hierarchical clustering
# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage


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
# CELL 5: CREATE DENDROGRAM
# =====================================================

# Create linkage matrix
linked = linkage(X_scaled, method="ward")

# Plot dendrogram
plt.figure(figsize=(10, 6))

dendrogram(linked)

plt.title("Dendrogram")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")

plt.show()


# =====================================================
# CELL 6: APPLY HIERARCHICAL CLUSTERING
# =====================================================

# Select number of clusters
hc = AgglomerativeClustering(
    n_clusters=3,
    linkage="ward"
)

# Train the model and assign clusters
data["Cluster"] = hc.fit_predict(X_scaled)

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

plt.figure(figsize=(8, 5))

plt.scatter(
    X_scaled[:, 0],
    X_scaled[:, 1],
    c=data["Cluster"]
)

plt.title("Hierarchical Clustering of Sales Data")
plt.xlabel("Sales (Normalized)")
plt.ylabel("Quantity Ordered (Normalized)")

plt.show()

#===== END OF PROGRAM=====


#=== VIVA Questions===
"""
1. Basic Concepts
1. What is Clustering?
Clustering is an unsupervised machine learning technique used to group similar data points together.

2. What is Unsupervised Learning?
Unsupervised learning uses unlabelled data to discover hidden patterns or groups.

3. What is K-Means Clustering?
K-Means is an unsupervised algorithm that divides data into K clusters based on similarity.

4. Why is K-Means called K-Means?
Because it creates K clusters and calculates the mean (centroid) of each cluster.

5. What is a Cluster?
A cluster is a group of data points that are similar to each other.

6. What is a Centroid?
A centroid is the center point of a cluster, calculated as the mean of all points in that cluster.

7. What is the main objective of K-Means?
To group similar data points while minimizing the distance between data points and their cluster centroids.

8. Is K-Means supervised or unsupervised?
Unsupervised learning because it does not require labelled output data.

2. Algorithm and Elbow Method

Q. Explain the working of the K-Means algorithm.
1. Select the number of clusters K.
2. Initialize K centroids.
3. Assign each data point to its nearest centroid.
4. Recalculate the centroids.
5. Repeat until the clusters stop changing significantly.

Q. Important differences between K-Means and Hierarchical Clustering:
K-Means	                             Hierarchical
Requires K beforehand	             Can visualize clusters using a dendrogram
Uses centroids	                     Uses distances between clusters
Iteratively updates centroids	     Merges or splits clusters
Generally faster for large datasets	|Can be computationally expensive

10. What is the Elbow Method?
The Elbow Method is used to determine the optimal number of clusters by plotting WCSS against different K values.

11. What is WCSS?
WCSS stands for Within-Cluster Sum of Squares. It,
measures the sum of squared distances between data points & their cluster centroids.

12. Why does WCSS decrease when K increases?
Because more clusters generally mean data points are closer to their respective centroids.

13. What does the elbow point represent?
It, represents the point where increasing the number of clusters provides significantly less improvement 
In, reducing WCSS.

14. Why did you select K = 3?
Based on the elbow graph, K = 3 is selected as the chosen number of clusters. The exact choice should be confirmed by observing the plotted graph.

15. What happens if K is too small?
Different groups may get combined into fewer clusters, resulting in under-segmentation.

16. What happens if K is too large?
Similar groups may get divided into too many small clusters.
3. Dataset and Features
17. Which dataset did you use?
The sales_data_sample.csv dataset.

18. Which features did you select?
- SALES
- QUANTITYORDERED
- PRICEEACH
- MSRP
19. What is the purpose of SALES?
It represents the total sales amount for an order record.

20. Why did you select numerical features?
K-Means calculates distances mathematically, so it requires numerical input features.

21. What is the purpose of StandardScaler?
It standardizes numerical features so they have approximately zero mean and unit variance.

22. Why is normalization important in K-Means?
Because K-Means uses distance calculations. Features with larger numerical values could otherwise dominate the clustering results.
4. Python Code-Based Questions
23. Why did you use encoding="latin1"?
To correctly read special characters in the dataset that may not be supported by the default UTF-8 encoding.

24. What does data.shape return?
It returns the number of rows and columns in the dataset.

25. What does fit_transform() do?
It calculates the scaling parameters from the data and transforms the data into standardized values.

26. What is random_state=42?
It ensures reproducible results by controlling the random initialization of centroids.

27. What is n_init=10?
It runs K-Means 10 times with different centroid initializations and selects the best result.

28. What does kmeans.inertia_ return?
It, returns the WCSS value for the fitted K-Means model.

29. What does kmeans.labels_ contain?
It contains the cluster number assigned to each data point.

30. What does data["Cluster"].value_counts() do?
It displays the number of records assigned to each cluster.

Q.Hirearchical Clustering 
It, uses Agglomerative Hierarchical Clustering and a Dendrogram to determine the optimal number of clusters.
"""
