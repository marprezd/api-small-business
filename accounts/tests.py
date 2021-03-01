# api-small-business/accounts/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomUserTests(TestCase):
    """This class extends TestCase and tests whether users can be created with or
    without administrative privileges.

    Args:
        TestCase ([type]): [description]
    """
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='testuser@testuser.com',
            password='password12345'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@testuser.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='testadmin',
            email='testadmin@testadmin.com',
            password='password12345'
        )
        self.assertEqual(admin_user.username, 'testadmin')
        self.assertEqual(admin_user.email, 'testadmin@testadmin.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
