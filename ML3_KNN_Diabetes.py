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


#===== viva questions====
"""
Evaluation Questions

Q34. What is Accuracy?
Ans: Accuracy measures the percentage of correctly predicted results.
Accuracy= TP+TN / TP+TN+FP+FN x 100

Q35. What is Error Rate?

Ans: Error Rate measures the percentage of incorrectly predicted results.
     Error Rate=1-Accuracy

Q47. What is Precision?
Ans: Precision measures how many of the model's positive predictions are actually correct.
->   P = TP/TP+NP

Q48. What is Recall?
Ans: Recall measures how many actual positive cases are correctly identified by the model.
Recall = TP/ TP + FN

Q38. What is the difference between Precision and Recall?
Ans:
- Precision focuses on how many predicted positive cases are correct.
- Recall focuses on how many actual positive cases are correctly identified.

Q3. What type of Machine Learning is used?
Ans: Supervised Learning.

Q4. What is KNN?
Ans: K-Nearest Neighbors is a supervised machine learning algorithm that classifies a data point based on the majority class of its nearest neighbors.

Q5. What type of classification is used?
Ans: Binary Classification.

Q6. What is the target variable in this dataset?
Ans: Outcome.
- 0 = No Diabetes.
- 1 = Diabetes.

2. KNN Algorithm Questions
Q9. How does the KNN algorithm work?

Ans:
1. Select the value of K.
2. Calculate the distance between data points.
3. Find the K nearest neighbors.
4. Count their classes.
5. Assign the majority class as the prediction.
Q10. What does K represent in KNN?

Ans: K represents the number of nearest neighbors considered for classification.

Q11. What is the value of K in our program?

Ans: K = 5.

Q12. Why do we use K = 5?

Ans: It is a commonly used starting value that considers five nearest neighbors for classification.

Q13. What is Euclidean Distance?
Ans: It is the straight-line distance between two data points.

Q14. What happens if K is too small?

Ans: The model may become sensitive to noise and overfit.

Q15. What happens if K is too large?

Ans: The model may become too generalized and underfit.

Q16. Is KNN a supervised or unsupervised algorithm?

Ans: KNN is a supervised learning algorithm.

Q17. Is KNN a lazy learning algorithm?

Ans: Yes. It stores the training data and performs calculations when making predictions.
3. Code-Based Viva Questions
Q18. Why do we import Pandas?

Ans: To read and manipulate the dataset.

Q19. What does pd.read_csv() do?

Ans: It reads a CSV file and loads it into a DataFrame.

Q20. What does data.head() display?

Ans: It displays the first five rows of the dataset by default.

Q21. What does data.shape return?

Ans: It returns the number of rows and columns in the dataset.

Q22. What does data.drop("Outcome", axis=1) do?

Ans: It removes the Outcome column from the dataset and stores the remaining columns as input features.

Q23. What is the purpose of X and y?

Ans:
- X contains input features.
- y contains the target variable.
Q24. What does test_size=0.2 mean?

Ans: It means 80% of the data is used for training and 20% for testing.

Q25. What is random_state=42?

Ans: It ensures reproducibility by maintaining the same random data split.

Q26. What is the purpose of stratify=y?

Ans: It maintains the same proportion of both classes in training and testing datasets.

Q27. Why do we use StandardScaler()?

Ans: To standardize features so that larger numerical values do not dominate distance calculations.

Q28. What is the difference between fit_transform() and transform()?

Ans:
- fit_transform() learns scaling parameters and transforms training data.
- transform() applies the same parameters to testing data.

Q29. What does KNeighborsClassifier(n_neighbors=5) do?
Ans: It initializes a KNN classifier that considers the five nearest neighbors.

Q30. What does knn.fit(X_train, y_train) do?

Ans: It trains the KNN model using the training data.

Q31. What does knn.predict(X_test) do?

Ans: It predicts whether the test samples belong to class 0 or class 1.

4. Evaluation Metrics Questions
Q32. What is a Confusion Matrix?

Ans: A Confusion Matrix is a table used to evaluate a classification model by comparing actual and predicted values.

Q33. What are TP, TN, FP, and FN?

Ans:
- TP (True Positive): Correctly predicted positive class.
- TN (True Negative): Correctly predicted negative class.
- FP (False Positive): Predicted positive when the actual class is negative.
- FN (False Negative): Predicted negative when the actual class is positive.

Q40. What is Overfitting?

Ans: Overfitting occurs when a model performs well on training data but poorly on unseen testing data.

Q41. What is Underfitting?

Ans: Underfitting occurs when a model is too simple to learn patterns and performs poorly on both training and testing data.

Q42. What is the difference between Classification and Regression?

Ans:
- Classification predicts categories.
- Regression predicts continuous numerical values.

Q3. What type of Machine Learning problem is this?
Ans: Supervised Learning and Binary Classification.

Q4. What is Binary Classification?
Ans: Binary Classification is a classification problem in which the output has only two possible classes.

Q1. What is Supervised Learning?
Ans: Supervised Learning is a type of Machine Learning in which a model is trained using labelled data (input with correct output).

Example: Spam Email Classification.

Q2. What is Unsupervised Learning?
Ans: Unsupervised Learning is a type of Machine Learning in which a model learns patterns from unlabelled data without predefined outputs.
Example: Customer Segmentation using K-Means.

Q3. What is Classification?
Ans: Classification is a Supervised Learning technique used to predict categories or classes.
Example: Spam or Not Spam.
Types of Classification:
1. Binary Classification: Two classes (Spam / Not Spam).
2. Multiclass Classification: More than two classes (Red / Green / Blue).
3. Multilabel Classification: One data point can belong to multiple classes.

Q4. What is Regression?
Ans: Regression is a Supervised Learning technique used to predict continuous numerical values.
Example: House Price Prediction.
Types of Regression:
1. Linear Regression: Predicts output using a straight-line relationship.
2. Multiple Linear Regression: Uses multiple input features.
3. Polynomial Regression: Models curved relationships.
4. Logistic Regression: Used for classification despite its name.

"""
