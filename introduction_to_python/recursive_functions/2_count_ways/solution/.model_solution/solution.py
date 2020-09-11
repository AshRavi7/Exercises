def fibo(n): 
    return n if n <= 1 else fibo(n-1) + fibo(n-2)

def count_ways(steps): 
    return fibo(steps + 1)

