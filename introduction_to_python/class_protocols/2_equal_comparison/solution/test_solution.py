def test_solution():
    import solution

    vector_a = solution.Vector3D(-9, -9, 5)
    vector_b = solution.Vector3D(11, 11, 3)
    vector_c = solution.Vector3D(11, 11, 3)

    assert vector_c == vector_c
    assert not (vector_a == vector_b)
    assert not (vector_a == vector_c)
    