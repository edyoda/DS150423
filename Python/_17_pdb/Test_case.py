from _2_pytest_demo import *

def test_add_int():
    assert add(3,1) == 4

def test_add_str():
    assert add("a","b") == "abc"

class TestCase:
    def test_add_int(self):
        assert add(3,1) == 45

    def test_add_str(self):
        assert add("a","b") == "ab"