# Define a recursive Python function named `count_down_from`
#  that consumes one argument `num`. 
# The function prints the numbers from `1` to `number` (inclusive)
#  in descending order, one on each line.
#  Do not use iteration of any form for this question.


# Write your solution here
def count_down_from(num):
    if num>=1:
        print(num)
        count_down_from(num-1)
    return