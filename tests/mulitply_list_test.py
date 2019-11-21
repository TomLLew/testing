import pytest
from python_exercises import multiply_list

def test_multiply_list():
    assert multiply_list.product([3, 3])==9

def test_multiply_list_one():
    assert multiply_list.product([5, 5])==25

def test_multiply_list_two():
    assert multiply_list.product([5, 5, 3])==75

def test_multiply_list_three():
    assert multiply_list.product([10, 5, 2, 3])==300

