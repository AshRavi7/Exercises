def test_solution():
    import solution
    assert solution.factorial_recursive(4) == 24
    assert solution.factorial_recursive(8) == 40320
    assert solution.factorial_recursive(0) == 1