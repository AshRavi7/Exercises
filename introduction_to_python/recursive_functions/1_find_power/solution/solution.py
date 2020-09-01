# Define a recursive Python function named `power` that consumes two parameters `a` and `b`.
# The function returns `a` to the power of `b`. Do not use the `**` operator or iteration in this question.

# Write your solution here
def power(a, b):
    if b == 1:
        return a
    return a * power(a, b-1)


# print(power(2,3))