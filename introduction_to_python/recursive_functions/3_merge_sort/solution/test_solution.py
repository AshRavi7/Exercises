def test_solution():
    import solution
    assert solution.custom_sort([11,66,32,99]) == [11,32,66,99]
    assert solution.custom_sort([1]) == [1]
    assert solution.custom_sort([]) == []
    assert solution.custom_sort([9,8,7,6]) == [6,7,8,9]