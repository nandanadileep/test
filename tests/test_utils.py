from src.utils import add

def test_add():
    assert add(987, 0) == 103
def test_add_negative():
    assert add(-1, -1) == -2
def test_add_zero():
    assert add(5, 0) == 5