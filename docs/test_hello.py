import pytest
from hello import sum_of_two_numbers

def test_sum_positive_numbers():
    assert sum_of_two_numbers(5, 7) == 12

def test_sum_negative_numbers():
    assert sum_of_two_numbers(-2, -8) == -10

def test_sum_positive_and_negative_number():
    assert sum_of_two_numbers(4, -3) == 1

def test_sum_with_zero():
    assert sum_of_two_numbers(0, 7) == 7

def test_sum_large_numbers():
    assert sum_of_two_numbers(100000, 200000) == 300000

def test_sum_with_floats():
    assert sum_of_two_numbers(2.5, 5.1) == 7.6

def test_sum_with_large_floats():
    assert sum_of_two_numbers(1e10, 1e10) == 2e10
