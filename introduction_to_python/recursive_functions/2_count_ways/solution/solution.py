def count_ways(steps):
    if steps == 0 or steps == 1:
      return 1
    return count_ways(steps-1) + count_ways(steps-2)