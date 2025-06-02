from django.test import TestCase
from .models import Course

class CourseModelTest(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            title="Test Course",
            description="This is a test course description."
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, "Test Course")
        self.assertEqual(self.course.description, "This is a test course description.")
        self.assertIsNotNone(self.course.created_at)
        self.assertIsNotNone(self.course.updated_at)

    def test_course_str(self):
        self.assertEqual(str(self.course), "Test Course")
