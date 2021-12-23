import pytest

@pytest.fixture
def data():
    return [1, 2, 3]


def test_1(data):
    assert 1==data[0]


@pytest.mark.xfail
def test_2(data):
    assert 3==data[1]


@pytest.mark.skip
def test_3(data):
    assert 3==data[2]