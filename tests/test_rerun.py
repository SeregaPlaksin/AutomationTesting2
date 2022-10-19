import pytest
import random


numbers = [1, 2, 3, 4, 5, 6]


def test_1():
    assert 1 == random.choice(numbers)