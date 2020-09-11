def test_solution():
    import solution

    vector_a = solution.Vector3D(1, 2, 0)
    vector_b = solution.Vector3D(y=1, z=3)
    vector_c = solution.Vector3D()

    assert (vector_a - vector_b).x == 1
    assert (vector_a - vector_b).y == 1
    assert (vector_a - vector_b).z == -3

    assert (vector_a - vector_c).x == 1
    assert (vector_a - vector_c).y == 2
    assert (vector_a - vector_c).z == 0