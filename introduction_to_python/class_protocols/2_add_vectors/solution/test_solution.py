def test_solution():
    import solution

    vector_a = solution.Vector3D(2, 4, 6)
    vector_b = solution.Vector3D(y=3, z=2)

    assert (vector_a + vector_b).x == 2
    assert (vector_a + vector_b).y == 7
    assert (vector_a + vector_b).z == 8
