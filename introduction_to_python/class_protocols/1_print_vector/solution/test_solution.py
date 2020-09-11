def test_solution():
    import solution

    vector_a = solution.Vector3D(4,5,6)
    assert str(vector_a) == '(x = 4, y = 5, z = 6)'

    vector_b = solution.Vector3D(y=0, z=1)
    assert str(vector_b) == '(x = 0, y = 0, z = 1)'

    vector_c = solution.Vector3D()
    assert str(vector_c) == '(x = 0, y = 0, z = 0)'