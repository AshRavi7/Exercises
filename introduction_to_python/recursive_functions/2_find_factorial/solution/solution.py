# Define a recursive Python function named `factorial_recursive` that consumes a number `n` and returns the factorial of `n`.

# Write your solution here
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    return n * factorial_recursive(n-1)

# print(factorial_recursive(10))