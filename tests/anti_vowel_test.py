import pytest
from python_exercises import anti_vowel

def test_anti_vowel():
    assert anti_vowel.anti_vowel("daviddavid")=="dvddvd"

def test_anti_vowel_one():
    assert anti_vowel.anti_vowel("john")=="jhn"

def test_anti_vowel_two():
    assert anti_vowel.anti_vowel("Thomas")=="Thms"

def test_anti_vowel_three():
    assert anti_vowel.anti_vowel("Leeroy")=="Lry"
