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

#=====VIVA Questions====
"""
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

Q6. What is KNN?
Ans: K-Nearest Neighbors is 
     a supervised machine learning algorithm that classifies 
     a data point based on the majority class of its nearest neighbors.

Q7. What is SVM?
Ans: Support Vector Machine is a supervised machine learning algorithm that finds the best decision boundary to separate different classes.

Q9. What is the target variable in this dataset?

Ans: Prediction, which represents whether an email is spam or not spam.

Q10. What do 0 and 1 represent in the target variable?

Ans:
- 0 = Not Spam.
- 1 = Spam.

Q12. What are features in Machine Learning?

Ans: Features are the input variables used by a machine learning model to make predictions.

Q13. What is Train-Test Split?

Ans: It divides the dataset into training data and testing data.

Q14. What does test_size=0.2 mean?

Ans: It means 80% of the data is used for training and 20% for testing.

Q15. What is the purpose of stratify=y?
Ans: It, maintains the same class distribution in both training and testing datasets.
     Data Normalization Questions

Q16. What is Normalization?
Ans: Normalization is the process of scaling features to a common range or distribution.

Q17. Why do we use StandardScaler?
Ans: StandardScaler standardizes features by subtracting the mean and dividing by the standard deviation.

Q18. What is the formula of StandardScaler?
->   Z = Originial Value - Mean / Standard Deviation

KNN Questions
Q20. What is K-Nearest Neighbors?

Ans: KNN classifies 
     a new data point based on the majority class 
     of its K nearest data points.

Q21. What does K represent in KNN?
Ans: K represents the number of nearest neighbors considered for classification.

Q22. What is the value of K in our program?
Ans: K = 5.

Q23. Why do we use K = 5?
Ans: It, is a commonly used starting value that considers five nearest neighbors for classification. 
     The best value can be found through hyperparameter tuning.

Q24. How does KNN classify an email?

Ans: It calculates the distance between the new email and existing training emails, selects the five nearest neighbors, and assigns the majority class.

Q25. What is Euclidean Distance?

Ans: Euclidean Distance measures the straight-line distance between two data points. 
d= root[(x2−x1)^2+(y2−y1)^2]


Q26. What happens if K is too small?
Ans: The model may become sensitive to noise and overfit.

Q27. What happens if K is too large?
Ans: The model may become too generalized and underfit.

SVM Questions
Q28. What is Support Vector Machine?
Ans: SVM is an algorithm that finds an optimal decision boundary to separate different classes.

Q29. What is a Hyperplane?
Ans: A hyperplane is a decision boundary that separates data points belonging to different classes.

Q30. What are Support Vectors?
Ans: Support Vectors are the data points closest to the decision boundary. They help determine its position.

Q31. What is a Kernel in SVM?
Ans: A Kernel is a function that helps SVM separate data that may not be linearly separable in the original feature space.

Q32. What is the Linear Kernel?
Ans: A Linear Kernel separates classes using a straight-line decision boundary in two dimensions or 
a    hyperplane in higher dimensions.

Q33. Why do we use kernel="linear"?
Ans: To, create an SVM model that uses a linear decision boundary.
     Code-Based Questions

Q34. What does pd.read_csv() do?
Ans: It reads a CSV file and loads it into a Pandas DataFrame.

Q35. What does data.head() display?
Ans: It displays the first five rows of the dataset by default.

Q36. What does data.shape return?
Ans: It returns the number of rows and columns in the dataset.

Q37. What does data.drop("Email No.", axis=1) do?
Ans: It removes the Email No. column from the dataset.

Q38. What does X = data.drop("Prediction", axis=1) do?
Ans: It stores all input features by removing the target column.

Q39. What does y = data["Prediction"] do?
Ans: It, stores the target variable.

Q40. What does knn.fit(X_train, y_train) do?
Ans: It, trains the KNN model using the training data.

Q41. What does svm.fit(X_train, y_train) do?
Ans: It, trains the SVM model using the training data.

Q42. What does predict() do?
Ans: It, predicts the output class for the testing data.

Q43. What does accuracy_score() calculate?
Ans: It, calculates the percentage of correctly classified predictions.

Q44. What does classification_report() display?
Ans: It, displays precision, recall, F1-score, and support for each class.

Q45. What does confusion_matrix() display?
Ans: It, displays the number of correct and incorrect predictions for each class.

Q46. What does if knn_accuracy > svm_accuracy do?
Ans: It, compares the accuracy of both models to identify which model performs better based on accuracy.

Q9. How does the KNN algorithm work?

Ans:
1. Select the value of K.
2. Calculate the distance between data points.
3. Find the K nearest neighbors.
4. Count their classes.
5. Assign the majority class as the prediction.

Evaluation and Advanced Questions
Q47. What is Precision?
Ans: Precision measures how many of the model's positive predictions are actually correct.
->   P = TP/TP+NP

Q48. What is Recall?
Ans: Recall measures how many actual positive cases are correctly identified by the model.
Recall = TP/ TP + FN

Q49. What is F1-Score?
Ans: F1-Score is the harmonic mean of Precision and Recall.
F1=2 x Prcision x Recall / Prcision + Recall


Q50. What are TP, TN, FP, and FN?

Ans:
- TP (True Positive): Correctly predicted positive class.
- TN (True Negative): Correctly predicted negative class.
- FP (False Positive): Predicted positive when the actual class is negative.
- FN (False Negative): Predicted negative when the actual class is positive.

Q51. Which algorithm is better, KNN or SVM?
Ans: It depends on the dataset. We compare their accuracy, precision, recall, and F1-score to determine which performs better.

Q52. What is Overfitting?
Ans: Overfitting occurs when a model performs well on training data but poorly on unseen testing data.

Q53. What is Underfitting?
Ans: Underfitting occurs when a model is too simple to learn the patterns in the data and performs poorly on both training and testing data.

Q54. What is the difference between KNN and SVM?
Ans:
KNN	                           SVM
Distance-based algorithm	   Boundary-based algorithm
Uses nearest neighbors	       Uses a hyperplane
Lazy learning algorithm	       Eager learning algorithm
Sensitive to feature scaling   Sensitive to feature scaling

Q55. Where is Email Spam Classification used?
Ans: It is used in email services such as Gmail and Outlook to detect unwanted or suspicious emails.
"""
