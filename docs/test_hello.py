import pytest
from hello import sum_of_two_numbers

def test_sum_of_two_positive_numbers():
    assert sum_of_two_numbers(3, 5) == 8

def test_sum_with_zero():
    assert sum_of_two_numbers(0, 7) == 7
    assert sum_of_two_numbers(5, 0) == 5

def test_sum_of_two_negative_numbers():
    assert sum_of_two_numbers(-3, -5) == -8

def test_sum_of_negative_and_positive_numbers():
    assert sum_of_two_numbers(-4, 6) == 2

def test_sum_of_large_numbers():
    assert sum_of_two_numbers(1000000, 2000000) == 3000000

def test_sum_of_boundary_case():
    assert sum_of_two_numbers(float('inf'), 0) == float('inf')
    assert sum_of_two_numbers(float('-inf'), 0) == float('-inf')

def test_sum_of_floats():
    assert sum_of_two_numbers(1.5, 2.5) == 4.0
    assert sum_of_two_numbers(-1.1, 1.1) == 0.0

def test_invalid_input_type():
    with pytest.raises(TypeError):
        sum_of_two_numbers('a', 5)
    with pytest.raises(TypeError):
        sum_of_two_numbers(5, 'b')
    with pytest.raises(TypeError):
        sum_of_two_numbers(None, 5)
