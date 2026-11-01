# **DAA-5:** Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.
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


#=====VIVA Questions====
"""
Basic Questions
Q1. What is the Knapsack Problem?

Ans: It is an optimization problem in which we select items to maximize total profit without exceeding the given knapsack capacity.

Q2. What is 0/1 Knapsack?

Ans: In 0/1 Knapsack, each item can either be selected completely (1) or not selected (0). We cannot take fractions of items.

Q3. Which algorithmic technique is used in this program?

Ans: Dynamic Programming.

Q4. What is Dynamic Programming?

Ans: Dynamic Programming is an algorithmic technique that solves a problem by dividing it into smaller subproblems and storing their results to avoid repeated calculations.

Q5. What is the main objective of 0/1 Knapsack?

Ans: To maximize total profit without exceeding the knapsack capacity.

Q6. What are the inputs required for this problem?

Ans: Number of items, weight of each item, profit of each item, and knapsack capacity.

Algorithm-Related Questions
Q7. Why do we use Dynamic Programming for 0/1 Knapsack?

Ans: Because the problem has overlapping subproblems and optimal substructure properties.

Q8. What is an overlapping subproblem?

Ans: It occurs when the same smaller subproblems are solved repeatedly.

Q9. What is optimal substructure?

Ans: It means that an optimal solution to a problem can be constructed using optimal solutions to its smaller subproblems.

Q10. What is the difference between 0/1 Knapsack and Fractional Knapsack?

Ans: In 0/1 Knapsack, we either take the complete item or leave it. In Fractional Knapsack, we can take a fraction of an item.

Q11. Why is Greedy not always optimal for 0/1 Knapsack?

Ans: Because selecting the item with the highest profit-to-weight ratio first may not produce the maximum total profit.
Program-Related Questions
Q12. Why do we create a 2D DP table?

Ans: To store the maximum profit for different numbers of items and different knapsack capacities.

Q13. Why is the DP table initialized with zeros?

Ans: Because the maximum profit is zero when there are no items or when the capacity is zero.

Q14. What does dp[i][j] represent?

Ans: It represents the maximum profit obtainable using the first i items with knapsack capacity j.

Q15. Why do we use range(1, n + 1)?

Ans: To process all items from the first item to the last item.

Q16. Why do we use weight[i - 1] and profit[i - 1]?

Ans: Because the DP table starts indexing items from 1, whereas Python lists start indexing from 0.

Q17. Explain the following statement:
dp[i][j] = max(    profit[i - 1] + dp[i - 1][j - weight[i - 1]],    dp[i - 1][j])



Ans: It calculates the maximum profit by comparing two possibilities:
- Include the current item.
- Exclude the current item.
Q18. What happens if the item's weight is greater than the current capacity?

Ans: The item cannot be included, so we copy the previous DP value.

Q19. Why do we use max() in this program?

Ans: To choose the option that gives the maximum profit between including and excluding an item.

Q20. What does dp[n][capacity] represent?

Ans: It represents the maximum profit that can be obtained using all items within the given capacity.
Complexity-Related Questions
Q21. What is the time complexity of this program?

Ans: O(n × W), where n is the number of items and W is the knapsack capacity.

Q22. What is the space complexity of this program?

Ans: O(n × W), because we create a 2D DP table of size (n+1) × (W+1).

Q23. Can we optimize the space complexity?

Ans: Yes. We can use a one-dimensional DP array and update it backwards, reducing space complexity to O(W).


Advanced Questions
Q24. What is the difference between Memoization and Tabulation?
Ans: Memoization is a top-down approach using recursion and caching, whereas Tabulation is a bottom-up approach using iteration.

Q25. What happens if the knapsack capacity is zero?
Ans: The maximum profit is zero because no item can be selected.

Q26. What happens if an item's weight is greater than the knapsack capacity?
Ans: That item cannot be selected.

Q27. What is the difference between Dynamic Programming and Greedy Algorithm?
Ans: Dynamic Programming considers multiple possibilities and stores their results, whereas Greedy selects the best local option at each step.

Q28. Where is the Knapsack Problem used?
Ans: It is used in resource allocation, cargo loading, investment planning, and budget optimization.
"""
