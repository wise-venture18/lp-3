#•	DAA-4: Write a program to solve a fractional Knapsack problem using a greedy method.
# Fractional Knapsack using Greedy Method

n = int(input("Enter number of items: "))

weight = []
profit = []
ratio = []

# Accept weight and profit of each item
for i in range(n):
    w = float(input("Enter weight: "))
    p = float(input("Enter profit: "))

    weight.append(w)
    profit.append(p)

    # Calculate profit/weight ratio
    ratio.append(p / w)

capacity = float(input("Enter knapsack capacity: "))

# Sort items according to ratio in descending order
for i in range(n):
    for j in range(i + 1, n):

        if ratio[i] < ratio[j]:

            # Swap ratios
            ratio[i], ratio[j] = ratio[j], ratio[i]

            # Swap corresponding weights
            weight[i], weight[j] = weight[j], weight[i]

            # Swap corresponding profits
            profit[i], profit[j] = profit[j], profit[i]

# Calculate maximum profit
total_profit = 0

for i in range(n):

    # If complete item fits in knapsack
    if weight[i] <= capacity:
        total_profit += profit[i]
        capacity -= weight[i]

    # If only a fraction of item fits
    else:
        total_profit += ratio[i] * capacity
        capacity = 0
        break

# Display maximum profit
print("Maximum Profit:", total_profit)

#---END----


#====SAMPLE INPUT====
"""
Enter number of items: 3

Enter weight: 10
Enter profit: 60

Enter weight: 20
Enter profit: 100

Enter weight: 30
Enter profit: 120

Enter knapsack capacity: 50

Maximum Profit: 240.0 """


#======VIVA Questions====
"""
Viva Questions and Answers
Basic Questions

Q1. What is the Knapsack Problem?
Ans: The Knapsack Problem is an optimization problem in which we select items to maximize total profit without exceeding the given capacity.

Q2. What is Fractional Knapsack?
Ans: Fractional Knapsack allows us to take either a complete item or a fraction of an item.

Q3. Which algorithmic technique is used in Fractional Knapsack?
Ans: Greedy Algorithm.

Q4. What is the main objective of Fractional Knapsack?
Ans: To maximize total profit within the given knapsack capacity.

Q5. What is the difference between Fractional and 0/1 Knapsack?
Ans: In Fractional Knapsack, we can take a fraction of an item, whereas in 0/1 Knapsack, we must either take the complete item or leave it.

Q6. What is the profit-to-weight ratio?

Ans: It, is the profit earned per unit of weight, calculated using: Ratio = Profit/Weight


Greedy Algorithm Questions
Q7. Why do we use the Greedy method in Fractional Knapsack?
Ans: Because selecting items with the highest profit-to-weight ratio first helps maximize the total profit.

Q8. Why do we sort items in descending order of ratio?
Ans: To select the most profitable items per unit of weight first.

Q9. What happens if the complete item fits in the knapsack?
Ans: We take the complete item and subtract its weight from the remaining capacity.

Q10. What happens if only a fraction of an item fits?
Ans: We take the fraction that fits, calculate its profit, and stop the algorithm.

Q11. Can we take half of an item in Fractional Knapsack?
Ans: Yes. We can take any fraction of an item.

Q12. Is Greedy Algorithm always optimal for Fractional Knapsack?
Ans: Yes. Selecting items in descending order of profit-to-weight ratio gives an optimal solution for Fractional Knapsack.

Program-Related Questions
Q13. Why do we use three lists: weight, profit, and ratio?

Ans: To store the weight, profit, and profit-to-weight ratio of each item.

Q14. What does ratio.append(p / w) do?

Ans: It calculates and stores the profit-to-weight ratio of an item.

Q15. Why do we use nested loops for sorting?

Ans: To arrange items in descending order of their profit-to-weight ratios.

Q16. Why do we swap weight, profit, and ratio together?

Ans: To maintain the correct relationship between each item's weight, profit, and ratio.

Q17. What does total_profit = 0 represent?
Ans: It initializes the total profit to zero.

Q18. Why do we use capacity -= weight[i]?

Ans: To reduce the remaining knapsack capacity after selecting a complete item.

Q19. Explain total_profit += ratio[i] * capacity.

Ans: It calculates the profit earned by taking a fraction of the current item that fits in the remaining capacity.

Q20. Why do we use break in the else condition?

Ans: Because the knapsack becomes full after taking the required fraction of the item, so no more items can be added.
Complexity-Related Questions
Q21. What is the time complexity of this program?

Ans: O(n²), because the nested loops are used for sorting the items.

Q22. What is the space complexity of this program?

Ans: O(n), because three lists are used to store item weights, profits, and ratios.

Q23. Can we improve the time complexity?

Ans: Yes. We can use Python's built-in sorting function to sort the items in O(n log n) time.

Advanced Questions
Q24. What is an optimal solution?
Ans: An optimal solution is the solution that provides the maximum possible profit within the given capacity.

Q25. What happens if the knapsack capacity is zero?
Ans: No items can be selected, and the maximum profit is zero.

Q26. What happens if the total weight of all items is less than the capacity?

Ans: All items can be selected, and the remaining capacity stays unused.

Q27. Where is the Knapsack Problem used?

Ans: It is used in resource allocation, cargo loading, investment planning, and budget optimization.

Q28. What is the difference between Greedy and Dynamic Programming?

Ans: Greedy makes the best local choice at each step, whereas Dynamic Programming solves and stores results of smaller subproblems.
"""
