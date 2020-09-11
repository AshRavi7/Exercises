def test_solution():
    import solution
    assert solution.reverse('everyone') == 'enoyreve'
    assert solution.reverse('hey') == 'yeh'
    assert solution.reverse('ok') == 'ko'
    assert solution.reverse('') == ''
