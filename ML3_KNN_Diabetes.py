"""
•	ML-3: Implement the K-Nearest Neighbors algorithm on the diabetes.csv dataset. Compute the confusion matrix, accuracy, error rate, precision and recall. 
o	Dataset link: https://www.kaggle.com/datasets/abdallamahgoub/diabetes OR https://drive.google.com/file/d/1gYSJj2AQeuVKDuGocEFLymvVf3t4H4pi/view?usp=sharing
"""

# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("diabetes.csv")

print("Dataset Loaded Successfully")
print(data.head())

print("\nDataset Shape:", data.shape)


# =====================================================
# CELL 3: SEPARATE FEATURES AND TARGET
# =====================================================

# X contains input features
X = data.drop("Outcome", axis=1)

# Y contains output
y = data["Outcome"]

print("\nFeatures and Target Separated")


# =====================================================
# CELL 4: SPLIT TRAINING AND TESTING DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# =====================================================
# CELL 5: NORMALIZE DATA
# =====================================================

scaler = StandardScaler()

# Fit and transform training data
X_train = scaler.fit_transform(X_train)

# Transform testing data
X_test = scaler.transform(X_test)

print("\nData Normalized Successfully")


# =====================================================
# CELL 6: BUILD AND TRAIN KNN MODEL
# =====================================================

# Select number of neighbors
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(X_train, y_train)

print("\nKNN Model Trained Successfully")


# =====================================================
# CELL 7: MAKE PREDICTIONS
# =====================================================

y_pred = knn.predict(X_test)

print("\nPredictions Completed")


# =====================================================
# CELL 8: CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# =====================================================
# CELL 9: CALCULATE PERFORMANCE METRICS
# =====================================================

accuracy = accuracy_score(y_test, y_pred)

error_rate = 1 - accuracy

precision = precision_score(y_test, y_pred, zero_division=0)

recall = recall_score(y_test, y_pred, zero_division=0)

print("\n===== PERFORMANCE METRICS =====")

print("Accuracy:", accuracy * 100, "%")

print("Error Rate:", error_rate * 100, "%")

print("Precision:", precision * 100, "%")

print("Recall:", recall * 100, "%")
