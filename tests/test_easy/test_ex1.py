import pytest


@pytest.mark.skip
def test_example():
    print('test1')
    assert 1 == 1


@pytest.mark.xfail
def test_example1():
    print('test2')
    assert 2 == 1


@pytest.mark.slow
def test_example2():
    print('test2')
    assert 1 == 1


@pytest.fixture(scope='session')
def fixture_1():
    print('run fixture_1')
    return 1


def test_fixture_1(fixture_1):
    print('test_fixture_1')
    num = fixture_1
    assert num == 1


def test_fixture_2(fixture_1):
    print('test_fixture_2')
    num = fixture_1
    assert num == 1
