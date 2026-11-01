#- **DAA-1:** Write a non-recursive and a recursive program to calculate Fibonacci numbers and analyze their time and space complexity.

# Fibonacci Series Using Recursive and Non-Recursive Methods

# Recursive Function
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-Recursive Function
def fibonacci_non_recursive(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Main Program
print("===== Fibonacci Series =====")
print("1. Recursive Approach")
print("2. Non-Recursive Approach")

choice = int(input("Enter your choice: "))

n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive number.")

elif choice == 1:
    print("\nFibonacci Series (Recursive):")

    for i in range(n):
        print(fibonacci_recursive(i), end=" ")

elif choice == 2:
    print("\nFibonacci Series (Non-Recursive):")
    fibonacci_non_recursive(n)

else:
    print("Invalid choice! Please select 1 or 2.")

print()

#===== END==========



#======VIVA QUESTIONS=====
"""
### Basic Questions

Q1. What is the Fibonacci series?

A: Fibonacci series is a sequence in which each number is the sum of the previous two numbers. It starts with 0 and 1.

Q2. What is the output of the Fibonacci series for 10 terms?

A: `0 1 1 2 3 5 8 13 21 34`

Q3. What is recursion?

A: Recursion is a programming technique in which a function calls itself to solve a problem.

Q4. What is iteration?

A: Iteration is a process of repeatedly executing a block of code using loops such as `for` and `while`.

Q5. What is a base condition in recursion?

A: A base condition is the condition that stops recursive function calls. In our program, `n <= 1` is the base condition.

Q6. Why do we need a base condition?

A: Without a base condition, the function may call itself indefinitely and cause a stack overflow.

Q7. What is the difference between recursion and iteration?

A: Recursion uses function calls to repeat operations, whereas iteration uses loops.

### Program-Related Questions

Q8. Why do we initialize `a = 0` and `b = 1`?

A: Because 0 and 1 are the first two numbers of the Fibonacci series.

Q9. What does `a, b = b, a + b` do?

A: It updates both variables simultaneously. The next Fibonacci number is calculated by adding the previous two numbers.

Q10. What is the purpose of `range(n)`?

A: It executes the loop n times, starting from 0 and ending at n-1.

Q11. What does `end=" "` do in the print statement?

A: It prints numbers on the same line with a space instead of moving to a new line.

Q12. Why does the recursive function return `n` when `n <= 1`?

A: Because the first two Fibonacci numbers are 0 and 1, which are the base cases.

Q13. What happens if we enter 0 as the number of terms?

A: The program displays a message asking the user to enter a positive number.

Q14. What happens if we enter an invalid choice?

A: The program displays an invalid choice message.

### Complexity-Related Questions

Q15. What is time complexity?

A: Time complexity measures how the execution time of an algorithm grows with input size.

Q16. What is space complexity?

A: Space complexity measures how much additional memory an algorithm requires.

Q17. What is the time complexity of the recursive Fibonacci program?

A: O(2ⁿ), because it makes repeated recursive calls.

Q18. What is the time complexity of the non-recursive Fibonacci program?

A: O(n), because it uses a loop that executes n times.

Q19. Which approach is more efficient?

A: The non-recursive approach is more efficient because it has O(n) time complexity and O(1) auxiliary space complexity.

Q20. What is stack overflow?

A: Stack overflow occurs when the call stack exceeds its available memory, often due to excessive or infinite recursion.

### Advanced Questions

Q21. Can Fibonacci numbers be calculated using Dynamic Programming?

A: Yes. Dynamic Programming stores previously calculated Fibonacci numbers to avoid repeated calculations.

Q22. What is the difference between O(n) and O(2ⁿ)?

A: O(n) grows linearly with input size, whereas O(2ⁿ) grows exponentially.

Q23. Can we calculate Fibonacci numbers using a while loop?

A: Yes. We can use a while loop instead of a for loop to generate the series.
"""
