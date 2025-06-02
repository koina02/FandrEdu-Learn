from django.test import TestCase
from .models import User
from .serializers import UserSerializer

class UserSerializerTest(TestCase):

    def test_user_creation(self):
        data = {
            'username': 'qoinpy',
            'email': 'qoin@example.com',
            'password': 'securePass123',
            'role': 'student',
        }
        serializer = UserSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        user = serializer.save()

        # Check user fields
        self.assertEqual(user.username, data['username'])
        self.assertEqual(user.email, data['email'])
        self.assertEqual(user.role, data['role'])

        # Password should not be stored in plain text
        self.assertNotEqual(user.password, data['password'])
        self.assertTrue(user.check_password(data['password']))
