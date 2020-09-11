def test_solution():
    import solution

    vector_a = solution.Vector3D(1, 5, 3)
    vector_b = solution.Vector3D(4, 4, 1)
    vector_c = solution.Vector3D(1, 5, 2)
    assert vector_c < vector_a
    assert vector_b < vector_a
    assert not (vector_a < vector_c)
    
    assert vector_a > vector_c
    assert not (vector_b > vector_a)
    assert not (vector_c > vector_a)
    