from src.utils import add

def test_add():
    # ❌ BREAKING: Wrong expected value
    assert add(1, 2) == 5   # Should be 3, but we wrote 5
    
def test_add_negative():
    # ❌ BREAKING: Wrong expected value  
    assert add(-1, -1) == 0  # Should be -2, but we wrote 0

def test_add_zero():
    # ✅ This one is correct
    assert add(5, 0) == 5
