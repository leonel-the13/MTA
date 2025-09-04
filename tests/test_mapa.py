import unittest
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'templates/pages')


import subprocess

class TestMapa(unittest.TestCase):
    def test_mapa_html(self):
        # Gera o mapa antes de testar
        subprocess.run(['python3', 'src/mapa.py'], check=True)
        mapa_path = os.path.join(data_dir, 'mapa.html')
        self.assertTrue(os.path.exists(mapa_path))
        with open(mapa_path, 'r', encoding='utf-8') as f:
            html = f.read()
        self.assertIn('<html', html.lower())
        self.assertIn('folium', html.lower())

if __name__ == '__main__':
    unittest.main()
