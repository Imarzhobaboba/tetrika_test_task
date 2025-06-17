import pytest
from solution import strict

def test_correct_types():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b
    assert sum_two(1, 2) == 3

def test_incorrect_types():
    @strict
    def sum_two(a: int, b: int) -> int:
        return a + b
    with pytest.raises(TypeError):
        sum_two(1, "2")

def test_mixed_types():
    @strict
    def concat(a: str, b: str) -> str:
        return a + b
    with pytest.raises(TypeError):
        concat("1", 2)
