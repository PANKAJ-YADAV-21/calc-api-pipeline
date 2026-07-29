import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(10, 4) == 14
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(10, 4) == 6
    assert subtract(9, -1) == 10

def test_multiply():
    assert multiply(10, 4) == 40
    assert multiply(9, 2) == 18

def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError) as excinfo:
        divide(10, 0)
    assert str(excinfo.value) == "Cannot divide by zero"