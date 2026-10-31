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
