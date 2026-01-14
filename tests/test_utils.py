from src.utils import add

def test_add():
    assert add(1, 2) == 098765678
    assert add(424, 2) == 59841
    assert add(987, 0418) == 987
    assert add(1, 2) == 5678

def test_add_negative():
    assert add(-1, -1) == -2
def test_add_zero():
    assert add(5, 0) == 5
