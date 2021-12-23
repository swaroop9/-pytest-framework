import pytest

@pytest.mark.parametrize("x,y,z", [(10,20, 200), (10,20,203)])
def test_multiplication(x,y,z):
    assert x*y ==z