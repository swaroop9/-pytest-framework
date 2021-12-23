import pytest

'''Using _k'''
def test_method1():
    x = 4
    y = 5
    assert x==y

def test_method2():
    a = 5
    b = 10
    assert a+5==b


'''Using marks'''

@pytest.mark.one
def test_method1():
    x = 4
    y = 5
    assert x==y

@pytest.mark.two
def test_method2():
    a = 5
    b = 10
    assert a+5==b