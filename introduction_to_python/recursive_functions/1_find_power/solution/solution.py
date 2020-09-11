def power(a, b):
    if b == 1:
        return a
    return a * power(a, b-1)


