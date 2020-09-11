def test_solution():
    import solution

    vector_a = solution.Vector3D(6,7,8)
    assert vector_a.x == 6
    assert vector_a.y == 7
    assert vector_a.z == 8

    vector_b = solution.Vector3D(y=77, z=88)
    assert vector_b.x == 0
    assert vector_b.y == 77
    assert vector_b.z == 88

    vector_c = solution.Vector3D()
    assert vector_c.x == 0
    assert vector_c.y == 0
    assert vector_c.z == 0