from django.test import TestCase
from links.models import Link


class LinkModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.obj = Link.objects.create(full_link='https://vk.com')

    def test_full_link(self):
        self.assertEqual('https://vk.com', self.obj.full_link)

    def test_attr_created(self):
        self.assertTrue(hasattr(self.obj, 'created_at'))

    def test_attr_updated(self):
        self.assertTrue(hasattr(self.obj, 'updated_at'))

    def test_attr_shortened(self):
        self.assertTrue(hasattr(self.obj, 'shortened_link'))

    def test_shortened_link(self):
        self.assertEqual(len(self.obj.shortened_link), 6)
