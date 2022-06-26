import pytest

from pytest_factoryboy import register
from tests.test_factoryboy.factories import UserFactory, ProductFactory, CategoryFactory

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)


@pytest.fixture
def new_user3(db, user_factory):
    user = user_factory.create()
    return user
