import pytest


@pytest.fixture
def yield_fixture():
    print('start test')
    yield 6
    print('end test')


def test_example_yield_1(yield_fixture):
    print('run example-1')
    assert yield_fixture == 6
