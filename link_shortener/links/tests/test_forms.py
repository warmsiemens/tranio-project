from django.test import TestCase
from links.forms import AddLinkForm


class AddLinkFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'full_link': 'https://vk.com'}
        form = AddLinkForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {'full_link': 55}
        form = AddLinkForm(data=form_data)
        self.assertFalse(form.is_valid())
