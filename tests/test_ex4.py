import pytest

from django.contrib.auth.models import User


# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")

# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-password") is True

# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     print('create-user')
#     return user


# def test_set_check_password1(user_1):
#     print('check-user1')
#     assert user_1.username == "test-user"
#
#
# def test_set_check_password2(user_1):
#     print('check-user2')
#     assert user_1.username == "test-user"

##################################

# def test_new_user(new_user1):
#     print(new_user1.first_name)
#     assert new_user1.first_name == "MyName"
#
#
# def test_new_user_is_stuff(new_user2):
#     print(new_user2.is_staff)
#     assert new_user2.is_staff
##################################
# def test_new_user(user_factory):
#     user = user_factory.build()
#     print(user.username)
#     assert True
# @pytest.mark.django_db
# def test_new_user_create(db, user_factory):
#     user = user_factory.create()
#     print(user.username)
#     assert True


# @pytest.mark.django_db
# def test_new_user_create1(user_factory):
#     user = user_factory.build()
#     count = User.objects.all().count()
#     print(count)
#     print(user.username)
#     assert True
#################################

# def test_new_user(new_user1):
#     print(new_user1.username)
#     assert True

###########################

def test_product(db, product_factory):
    product = product_factory.create()
    print(product.description)
    assert True
