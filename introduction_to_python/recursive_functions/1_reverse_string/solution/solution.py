# Define a recursive Python function named `reverse` that consumes one argument `string`.
# The function returns the a string whos contents is the reverse of `string` 
# Do not use iteration of any form for this question.

# Write your solution here
def reverse(string):
    if string == "":
        return ""
    return string[-1] + reverse(string[:-1])

# print(reverse("hello"))