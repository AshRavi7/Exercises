def test_solution():
    import solution

    vector_a = solution.Vector3D(1, 2, 3)
    vector_b = solution.Vector3D(y=1, z=3)
    vector_c = solution.Vector3D()

    assert (vector_a * vector_b) == 11
    assert (vector_a * vector_c) == 0