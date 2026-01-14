from src.utils import greet, reverse_string

def test_greet():
    assert greet("World") == "Hi, World!"  # Wrong: should be "Hello, World!"

def test_greet_name():
    assert greet("Alice") == "Hello, Bob!"  # Wrong: should be "Hello, Alice!"

def test_reverse():
    assert reverse_string("hello") == "helo"  # Wrong: should be "olleh"

