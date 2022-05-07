from django.urls.base import reverse
from django.utils import timezone
from django.test import TestCase
from django.db.utils import IntegrityError

from .models import User

class UsersModelTest(TestCase):
    def test_two_users_equeal_email(self):
        """Two users cannot have the same email address"""
        try:
            user1 = User(user_name = 'user1', email = 'echo@example.com' , password = '12345').save()
            user2 = User(user_name = 'user2', email = 'echo@example.com' , password = '12345').save()
            self.assertTrue(False)
        except IntegrityError:
            self.assertTrue(True)

    def test_two_users_equeal_user_name(self):
        """Two users cannot have the same user name """
        try:
            user1 = User(user_name = 'user1', email = 'echo@example.com' , password = '12345').save()
            user2 = User(user_name = 'user1', email = 'echo2@example.com' , password = '12345').save()
            self.assertTrue(False)
        except IntegrityError:
            self.assertTrue(True)

def DoorContentModelTest(TestCase):
    def test_every_door_must_have_a_DoorContent(self):
        """Test to prove that every door must have a content inside it so that there are no empty doors."""
        pass
    

