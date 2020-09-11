import solution

def test_solution(monkeypatch):
    assert solution.sum_array(num_list=[4,5,6]) == 15
    assert solution.sum_array(num_list=[1,5,10.2]) == 16.2
    assert solution.sum_array(num_list=[]) == 0

