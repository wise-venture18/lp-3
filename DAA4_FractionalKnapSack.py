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
