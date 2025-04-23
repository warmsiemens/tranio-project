from django.test import TestCase
from links.models import Link
from django.urls import reverse


class AddLinkViewTest(TestCase):

    def test_add_link_view_status_code(self):
        url = reverse('add_link')
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)

    def test_add_link_view_template(self):
        url = reverse('add_link')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'links/link_add.html')

    def test_add_link_view_form(self):
        url = reverse('add_link')
        response = self.client.get(url)
        self.assertIn('form', response.context)

    def test_add_link_view_post(self):
        data = {'full_link': 'https://vk.com'}
        response = self.client.post(reverse('add_link'), data)

        self.assertTrue(Link.objects.filter(full_link='https://vk.com').exists())
        self.assertEqual(response.status_code, 200)


class StatsViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Link.objects.create(full_link='https://vk.com', shortened_link='qwerty')

    def test_stats_view_status_code(self):
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, 200)

    def test_stats_view_uses_correct_template(self):
        response = self.client.get(reverse('stats'))
        self.assertTemplateUsed(response, 'links/link_stats.html')

    def test_stats_view_context_contains_links(self):
        response = self.client.get(reverse('stats'))
        self.assertIn('links', response.context)
        self.assertEqual(len(response.context['links']), 1)


class RedirectLinkViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.link = Link.objects.create(full_link='https://vk.com', shortened_link='qwerty')

    def test_click_counter_incremented(self):
        self.assertEqual(self.link.count_of_clicks, 0)
        self.client.get(reverse('redirect_link', args=[self.link.shortened_link]))
        self.link.refresh_from_db()
        self.assertEqual(self.link.count_of_clicks, 1)

    def test_redirect_link_404_on_invalid_shortened(self):
        response = self.client.get(reverse('redirect_link', args=['invalid123']))
        self.assertEqual(response.status_code, 404)
