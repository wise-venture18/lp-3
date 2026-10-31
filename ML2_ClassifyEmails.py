#•	ML-2: Classify emails using binary classification: Normal State (Not Spam) and Abnormal State (Spam). Use K-Nearest Neighbors and Support Vector Machine, and analyze their performance. 
# Download Dataset : https://drive.google.com/file/d/1Ctx3bx0TGYshBtDdvSxWQvay9IEhj9t-/view?usp=sharing

# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("emails.csv")

print("Dataset Loaded Successfully")
print(data.head())

print("\nDataset Shape:", data.shape)


# =====================================================
# CELL 3: DATA PREPROCESSING
# =====================================================

# Remove unnecessary Email ID column
data = data.drop("Email No.", axis=1)

# Separate features and target
X = data.drop("Prediction", axis=1)
y = data["Prediction"]

print("\nFeatures and Target Separated")
print("Features Shape:", X.shape)
print("Target Shape:", y.shape)


# =====================================================
# CELL 4: SPLIT TRAINING AND TESTING DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining Data:", X_train.shape)
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
# CELL 6: K-NEAREST NEIGHBORS (KNN)
# =====================================================

# Initialize KNN model
knn = KNeighborsClassifier(n_neighbors=5)

# Train KNN model
knn.fit(X_train, y_train)

# Predict test data
knn_pred = knn.predict(X_test)

# Calculate accuracy
knn_accuracy = accuracy_score(y_test, knn_pred)

print("\nKNN Accuracy:", knn_accuracy * 100, "%")

print("\nKNN Confusion Matrix:")
print(confusion_matrix(y_test, knn_pred))


# =====================================================
# CELL 7: SUPPORT VECTOR MACHINE (SVM)
# =====================================================

# Initialize SVM model
svm = SVC(kernel="linear")

# Train SVM model
svm.fit(X_train, y_train)

# Predict test data
svm_pred = svm.predict(X_test)

# Calculate accuracy
svm_accuracy = accuracy_score(y_test, svm_pred)

print("\nSVM Accuracy:", svm_accuracy * 100, "%")

print("\nSVM Confusion Matrix:")
print(confusion_matrix(y_test, svm_pred))


# =====================================================
# CELL 8: CLASSIFICATION REPORT
# =====================================================

print("\nKNN Classification Report:")
print(classification_report(y_test, knn_pred))

print("\nSVM Classification Report:")
print(classification_report(y_test, svm_pred))


# =====================================================
# CELL 9: PERFORMANCE COMPARISON
# =====================================================

print("\n===== MODEL PERFORMANCE COMPARISON =====")

print("KNN Accuracy:", knn_accuracy * 100, "%")
print("SVM Accuracy:", svm_accuracy * 100, "%")

if knn_accuracy > svm_accuracy:
    print("\nKNN performs better.")
elif svm_accuracy > knn_accuracy:
    print("\nSVM performs better.")
else:
    print("\nBoth models have equal accuracy.")
