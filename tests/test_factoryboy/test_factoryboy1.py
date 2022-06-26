import pytest

from django.contrib.auth.models import User


def test_new_user(user_factory):
    user = user_factory.build()
    print(user.username)
    assert True


@pytest.mark.django_db
def test_new_user_create(db, user_factory):
    user = user_factory.create()
    print(user.username)
    assert True


@pytest.mark.django_db
def test_new_user_create1(user_factory):
    user = user_factory.build()
    count = User.objects.all().count()
    print(count)
    print(user.username)
    assert True


def test_new_user_factory(new_user3):
    print(new_user3.username)
    assert True


def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True
