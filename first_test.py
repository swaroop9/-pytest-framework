import pytest

def add(a,b):
    return a+b


def test_add():
    sum = add(1,3)
    assert sum == 4

