"""
Q.•	ML-1: Given a bank customer, build a neural network-based classifier that can determine whether they will leave or not in the next 6 months. 
o	Dataset: Kaggle bank customer churn (10,000 samples, 14 features such as CustomerId, CreditScore, Geography, Gender, Age, Tenure, Balance). Link: https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling
o	Steps: 
1.	Read the dataset.
2.	Separate the feature and target sets, and split into training and test sets.
3.	Normalize the train and test data.
4.	Initialize and build the model. Identify points of improvement and implement them.
5.	Print the accuracy score and confusion matrix (5 points).

Dataset Download : https://drive.google.com/file/d/1VxDUw9CG2Uac2N8pjojdDmQ8iTl4pVzB/view?usp=sharing
"""

# =====================================================
# CELL 1: IMPORT LIBRARIES
# =====================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping


# =====================================================
# CELL 2: READ DATASET
# =====================================================

data = pd.read_csv("Churn_Modelling.csv")

print("Dataset Loaded Successfully")
print(data.head())


# =====================================================
# CELL 3: DATASET INFORMATION
# =====================================================

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

print("\nDataset Shape:", data.shape)


# =====================================================
# CELL 4: DATA PREPROCESSING
# =====================================================

# Remove unnecessary columns
data = data.drop(["RowNumber", "CustomerId", "Surname"], axis=1)

# Convert categorical data into numerical data
data = pd.get_dummies(
    data, columns=["Geography", "Gender"], dtype=int
)

# Separate features and target
X = data.drop("Exited", axis=1)
y = data["Exited"]

print("\nFeatures and Target Separated")


# =====================================================
# CELL 5: SPLIT TRAINING AND TESTING DATA
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)


# =====================================================
# CELL 6: NORMALIZE DATA
# =====================================================

scaler = StandardScaler()

# Fit scaler on training data
X_train = scaler.fit_transform(X_train)

# Transform testing data
X_test = scaler.transform(X_test)

print("Data Normalized Successfully")


# =====================================================
# CELL 7: BUILD NEURAL NETWORK MODEL
# =====================================================

model = Sequential()

# First hidden layer
model.add(Dense(16, activation="relu",
                input_shape=(X_train.shape[1],)))

# Second hidden layer
model.add(Dense(8, activation="relu"))

# Dropout to reduce overfitting
model.add(Dropout(0.2))

# Output layer
model.add(Dense(1, activation="sigmoid"))

model.summary()


# =====================================================
# CELL 8: COMPILE MODEL
# =====================================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

print("Model Compiled Successfully")


# =====================================================
# CELL 9: TRAIN MODEL
# =====================================================

# Early stopping to prevent overfitting
early_stop = EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    epochs=30,
    batch_size=32,
    validation_split=0.2,
    callbacks=[early_stop]
)


# =====================================================
# CELL 10: MAKE PREDICTIONS
# =====================================================

predictions = model.predict(X_test)

# Convert probabilities into 0 or 1
y_pred = (predictions > 0.5).astype(int)

print("Predictions Completed")


# =====================================================
# CELL 11: CALCULATE ACCURACY
# =====================================================

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy * 100, "%")


# =====================================================
# CELL 12: CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# =====================================================
# CELL 13: POINTS OF IMPROVEMENT
# =====================================================

print("\nPoints of Improvement:")
print("1. Data Normalization using StandardScaler")
print("2. Multiple Hidden Layers")
print("3. Dropout to reduce Overfitting")
print("4. Early Stopping")
print("5. Adam Optimizer")



#=======VIVA Questions======
"""
Q9. What is Feature Selection?
Ans: Feature Selection is the process of selecting relevant input variables for training a machine learning model.

Q11. What is One-Hot Encoding?
Ans: One-Hot Encoding converts categorical values into separate binary columns.

Q12. Why do we use pd.get_dummies()?
Ans: To convert categorical columns such as Geography and Gender into numerical columns.

Data Normalization Questions
Q15. What is Normalization?
Ans: Normalization is the process of scaling features to a common range or distribution so that features with larger values do not dominate model training.

Q16. Why do we use StandardScaler?
Ans: StandardScaler standardizes features by subtracting the mean and dividing by the standard deviation.

Q17. What is the formula of StandardScaler?
->   z = Original value - Mean / Standard Deviation

Q18. Why do we use fit_transform() on training data and transform() on testing data?
Ans: To, calculate scaling parameters using training data only and apply the same parameters to testing data, preventing data leakage.

Neural Network Questions
Q19. What are the main layers of a Neural Network?
Ans:
1. Input Layer
2. Hidden Layer
3. Output Layer

Q20. What is an Activation Function?
Ans: An Activation Function determines whether and how strongly 
     a neuron should activate based on its input.

Q21. What is ReLU?
Ans: ReLU stands for Rectified Linear Unit. It returns zero for negative values and the same value for positive values.
     ReLU(x)= max(0,x)

Q22. Why do we use Sigmoid in the output layer?
Ans: Sigmoid converts the output into a probability between 0 and 1, making it suitable for binary classification.

Q23. What is Dropout?
Ans: Dropout is a regularization technique that randomly disables some neurons during training to reduce overfitting.

Q24. What is Overfitting?
Ans: Overfitting occurs when a model performs well on training data but poorly on unseen testing data.

Q28. What is Adam Optimizer?
Ans: Adam stands for Adaptive Moment Estimation. It,
     Is an optimization algorithm that adjusts the learning rate for model parameters.

Q29. What is a Loss Function?
Ans: A loss function measures the difference between actual and predicted outputs.

Q30. Why do we use Binary Crossentropy?
Ans: Because this is a binary classification problem with two possible outputs, 0 and 1.

Q31. What is Early Stopping?
Ans: Early Stopping stops model training when validation performance stops improving, helping prevent overfitting.

Q32. What does patience=5 mean?
Ans: Training stops if the monitored validation loss does not improve for 5 consecutive epochs.

Q33. What is Accuracy?
Ans: Accuracy = correct prediction/total prediction x 100

Q34. What is a Confusion Matrix?
Ans: A Confusion Matrix is a table used to evaluate 
     a classification model by comparing actual and 
     predicted values.

Q35. What are TP, TN, FP, and FN?
Ans:
- TP (True Positive): Model correctly predicts the positive class.
- TN (True Negative): Model correctly predicts the negative class.
- FP (False Positive): Model incorrectly predicts positive when the actual class is negative.
- FN (False Negative): Model incorrectly predicts negative when the actual class is positive.

Q17. What does axis=1 mean in data.drop()?
Ans: It indicates that columns should be removed. axis=0 is used to remove rows.

Q2. What is Underfitting?
Ans: Underfitting occurs when a machine learning model is too simple to learn the patterns in the training data, 
     resulting in poor performance on both training and testing data.

Q1. What is Precision?
Ans: P = TP/TP+FP

Q11. What does data.info() do?
Ans: It displays dataset information such as column names, data types, and non-null values.

Q27. What does Dense(16, activation="relu") mean?
Ans: It creates a fully connected hidden layer containing 16 neurons with ReLU activation.
