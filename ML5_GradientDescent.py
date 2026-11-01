# =====================================================
# CELL 1: IMPORT LIBRARY
# =====================================================

import matplotlib.pyplot as plt


# =====================================================
# CELL 2: DEFINE FUNCTION AND DERIVATIVE
# =====================================================

# Given function: y = (x + 3)^2

def function(x):
    return (x + 3) ** 2

# Derivative: dy/dx = 2(x + 3)

def derivative(x):
    return 2 * (x + 3)


# =====================================================
# CELL 3: INITIALIZE PARAMETERS
# =====================================================

x = 2               # Starting point
learning_rate = 0.1
iterations = 50

x_values = []
y_values = []


# =====================================================
# CELL 4: APPLY GRADIENT DESCENT
# =====================================================

for i in range(iterations):

    # Calculate gradient
    grad = derivative(x)

    # Update x value
    x = x - learning_rate * grad

    # Store values
    x_values.append(x)
    y_values.append(function(x))


# =====================================================
# CELL 5: DISPLAY LOCAL MINIMUM
# =====================================================

print("Minimum value of x:", x)
print("Minimum value of y:", function(x))


# =====================================================
# CELL 6: PLOT GRAPH
# =====================================================

plt.plot(x_values, y_values, marker='o')

plt.title("Gradient Descent")
plt.xlabel("Iterations")
plt.ylabel("Function Value")

plt.grid()
plt.show()



#====VIVA Questions====
"""
1. Basic Concepts
1. What is Gradient Descent?
Gradient Descent is an optimization algorithm used to find the minimum value of 
a function by repeatedly updating its parameters.

2. What is the main purpose of Gradient Descent?
To, minimize the cost or loss function and find its minimum value.

3. What is a Gradient?
A gradient represents the slope or rate of change of a function.

4. What is a Derivative?
A derivative measures how much a function changes when its input changes.

5. What is the Learning Rate?
The learning rate controls how big a step the algorithm takes while updating the value of a parameter.

6. What happens if the learning rate is too high?
The algorithm may overshoot the minimum and fail to converge.

7. What happens if the learning rate is too low?
The algorithm takes very small steps and requires more iterations to reach the minimum.

8. What is an Iteration?
One complete execution of the gradient descent update step.

9. What is a Local Minimum?
A point where the function has a lower value than nearby points.

10. What is a Global Minimum?
The lowest possible value of a function over its entire domain.

15. Why do we subtract the gradient?
Because subtracting the gradient moves the parameter in the direction of decreasing function value.

3. Python Code-Based Questions

16. Why did you import Matplotlib?
To, plot and visualize the gradient descent process.

17. What does function(x) return?
It, returns the value of the function \((x+3)^2\) for the given x.

18. What does derivative(x) return?
It, returns the gradient of the function at the given x.

19. Why is the initial value of x set to 2?
It provides the starting point from which gradient descent begins.

20. Why did you choose learning_rate = 0.1?
It controls the step size during updates and provides a reasonable rate of convergence for this example.

21. Why did you choose iterations = 50?
To repeat the update process 50 times so that x approaches the minimum.

22. What is the purpose of grad = derivative(x)?
It calculates the current gradient at the current value of x.

23. Explain x = x - learning_rate * grad.
It updates x by moving in the opposite direction of the gradient.

24. Why are x_values and y_values used?
They store the updated x values and corresponding function values for plotting.

25. What does x_values.append(x) do?
It stores the current updated x value in the list.

26. What does y_values.append(function(x)) do?
It stores the function value corresponding to the current x.

27. What does plt.plot() do?
It draws a graph using the stored x and y values.

28. What does marker='o' do?
It displays circular markers at each plotted data point.

29. What does plt.grid() do?
It displays grid lines on the graph.

30. What is the final output of your program?
The value of x approaches -3, and the function value approaches 0.

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
