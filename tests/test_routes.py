import unittest
from src.app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Turismo Acess', resp.data)

    def test_mapa_folium(self):
        resp = self.client.get('/mapa')
        self.assertEqual(resp.status_code, 200)
        self.assertIn(b'Mapa de Acessibilidade', resp.data)

if __name__ == '__main__':
    unittest.main()
