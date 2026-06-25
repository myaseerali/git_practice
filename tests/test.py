from src.mathsoperations import add, subt


def test_add():
    assert add(5, 3) == 8
    assert add(-5, 3)== 2
    assert add(-10, 20) == 10
    
    
    def test_subt():
        assert subt(25, 10)== 15
        assert subt(-5, 3)== -2
        assert subt(-5, -3)== -2
        assert subt(5, -3)== 8