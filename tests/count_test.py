import pytest
from python_exercises import count


def  test_count_zeros():
    assert count.count([0, 0, 0],0)==3

def test_count_string():
    assert count.count(["a", "a", "a"], "a")==3

def test_count_zeros_one():
    assert count.count([0, 1, 0, 2, 0, 0], 0)==4

def test_count_string_one():
    assert count.count(["a", "b", "a", "c", "a", "a"], "a")==4
