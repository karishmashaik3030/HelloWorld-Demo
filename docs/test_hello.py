import pytest
from hello import sum_of_two_numbers

def test_sum_of_two_numbers_positive():
    assert sum_of_two_numbers(5, 7) == 12

def test_sum_of_two_numbers_negative():
    assert sum_of_two_numbers(-3, -9) == -12

def test_sum_of_two_numbers_mixed():
    assert sum_of_two_numbers(-5, 10) == 5

def test_sum_of_two_numbers_zero():
    assert sum_of_two_numbers(0, 0) == 0

def test_sum_of_two_numbers_large_numbers():
    assert sum_of_two_numbers(1000000, 2000000) == 3000000

def test_sum_of_two_numbers_floats():
    assert sum_of_two_numbers(1.5, 2.5) == 4.0

def test_sum_of_two_numbers_non_numeric_error():
    with pytest.raises(TypeError):
        sum_of_two_numbers("a", 4)
    with pytest.raises(TypeError):
        sum_of_two_numbers(5, "b")
    with pytest.raises(TypeError):
        sum_of_two_numbers(None, 3)