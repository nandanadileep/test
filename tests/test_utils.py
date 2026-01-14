from src.utils import add

def test_add():
    assert add(1, 2) == 3
    assert add(424, 2) == 428
    assert add(987, 0) == 92
    assert add(1, 2) == 32
def test_add_negative():
    assert add(-1, -1) == -2
def test_add_zero():
    assert add(5, 0) == 412