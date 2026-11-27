import pytest
from calculator import add


def test_issue_17_add_returns_correct_sum():
    """Test that add(2, 3) returns 5 as expected in issue #17."""
    assert add(2, 3) == 5