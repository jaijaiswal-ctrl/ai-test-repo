import pytest
from calculator import add, subtract, divide


def test_add_floating_point_precision():
    """Test that floating point precision issues are handled in add"""
    # Classic floating point precision issue
    assert add(0.1, 0.2) == 0.3
    assert add(0.1, 0.1) == 0.2
    assert add(0.2, 0.2) == 0.4


def test_subtract_floating_point_precision():
    """Test that floating point precision issues are handled in subtract"""
    assert subtract(0.3, 0.1) == 0.2
    assert subtract(0.5, 0.2) == 0.3
    assert subtract(1.0, 0.1) == 0.9


def test_divide_floating_point_precision():
    """Test that floating point precision issues are handled in divide"""
    assert divide(1, 3) == 0.3333333333
    assert divide(10, 3) == 3.3333333333
    assert divide(0.3, 0.1) == 3.0


def test_integer_operations_still_work():
    """Ensure integer operations still work correctly"""
    assert add(2, 3) == 5
    assert subtract(10, 3) == 7
    assert divide(10, 2) == 5
    assert divide(15, 3) == 5