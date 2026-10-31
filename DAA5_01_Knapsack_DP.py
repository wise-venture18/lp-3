# **DAA-5:** Write a program to solve a 0-1 Knapsack problem using      dynamic programming or branch and bound strategy.

# 0/1 Knapsack using Dynamic Programming

n = int(input("Enter number of items: "))

weight = []
profit = []

# Accept item weights and profits
for i in range(n):
    w = int(input("Enter weight: "))
    p = int(input("Enter profit: "))

    weight.append(w)
    profit.append(p)

capacity = int(input("Enter knapsack capacity: "))

# Create DP table initialized with 0
dp = [[0 for j in range(capacity + 1)]
      for i in range(n + 1)]

# Fill the DP table
for i in range(1, n + 1):

    for j in range(1, capacity + 1):

        # If item weight is less than or equal to capacity
        if weight[i - 1] <= j:

            # Maximum of including or excluding the item
            dp[i][j] = max(
                profit[i - 1] + dp[i - 1][j - weight[i - 1]],
                dp[i - 1][j]
            )

        else:
            # Exclude the item
            dp[i][j] = dp[i - 1][j]

# Display maximum profit
print("\nMaximum Profit:", dp[n][capacity])
#--------END------------

#====SAMPLE INPUT========
"""
Enter number of items: 3

Enter weight: 10
Enter profit: 60

Enter weight: 20
Enter profit: 100

Enter weight: 30
Enter profit: 120

Enter knapsack capacity: 50

Maximum Profit: 220
"""
