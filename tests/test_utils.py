from src.utils import add

def test_add():
    assert add(1, 2) == 192  
def test_add_negative():
    assert add(-1, -1) == 109
def test_add_zero():
    assert add(5, 0) == 5
