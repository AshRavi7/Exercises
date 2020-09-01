# Assume you are climbing a stair case and it takes `n` steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# Write a recursive Python function named `count_ways` that consumes a number `steps`.
# The function returns the number of distinct ways to climb to the top.
# Hint: Make sure you attempt the question before trying this one!

# Write your solution here
def count_ways(steps):
    if steps == 0 or steps == 1:
      return 1
    return count_ways(steps-1) + count_ways(steps-2)