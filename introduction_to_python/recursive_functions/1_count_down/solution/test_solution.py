def test_solution(monkeypatch):
    return_val= []
    def g(num):
        return_val.append(num)
        
    monkeypatch.setattr('builtins.print',g)

    import solution
    solution.count_down_from(3)
    
    assert return_val[0] == 3
    assert return_val[1] == 2
    assert return_val[2] == 1
    assert len(return_val) == 3
    
    
