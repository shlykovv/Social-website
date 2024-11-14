import http

from django.test import Client, TestCase


class StaticURLTests(TestCase):
    '''Класс для тестирование url-адресов'''
    def setUp(self) -> None:
        self.guest_client = Client()

    def test_get_login_url(self):
        response = self.guest_client.get('/account/login/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_url_correct_template(self):
        response = self.guest_client.get('/account/login/')
        self.assertTemplateUsed(response, 'registration/login.html')
