import unittest

from ..app import weather


class TestWeather(unittest.TestCase):
    def setUp(self):
        app = weather.test_client()
        self.response = app.get('/weather/parana')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)
