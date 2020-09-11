def test_solution():
    import solution
    from math import sqrt as sq

    vector_a = solution.Vector3D(1, 5, 3)
    vector_b = solution.Vector3D(4, 4, 1)
    vector_c = solution.Vector3D(1, 5, 2)

    assert vector_a.magnitude() == sq(35)
    assert vector_b.magnitude() == sq(33)
    assert vector_c.magnitude() == sq(30)