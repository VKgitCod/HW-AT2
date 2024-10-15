import pytest
from main import number_of_vowels

@pytest.mark.parametrize('test_vowels, expected', [
    ('Python', 1),
    ('aouaaaa', 7),
    ('Sport', 1),
    ('Ttpbd', 0),
    ('', 0)
])
def test_number_of_vowels(test_vowels, expected):
    assert number_of_vowels(test_vowels) == expected