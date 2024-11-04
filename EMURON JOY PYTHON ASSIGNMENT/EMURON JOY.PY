def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

# Get user input
try:
    n = int(input("Enter a positive integer n to find the nth Fibonacci number: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is: {result}")
except ValueError:
    print("Invalid input. Please enter a positive integer.")


