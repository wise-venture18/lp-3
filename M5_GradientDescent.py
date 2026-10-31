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
