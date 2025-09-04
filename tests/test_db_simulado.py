import unittest
from src import db_simulado

class TestDbSimulado(unittest.TestCase):
    def test_get_atracoes(self):
        df = db_simulado.get_atracoes()
        self.assertFalse(df.empty)
        self.assertIn('nome', df.columns)
        self.assertIn('latitude', df.columns)
        self.assertIn('longitude', df.columns)
        self.assertIn('acessivel', df.columns)

    def test_get_atracoes_types(self):
        df = db_simulado.get_atracoes()
        self.assertTrue(df['latitude'].apply(lambda x: isinstance(x, float) or isinstance(x, int)).all())
        self.assertTrue(df['longitude'].apply(lambda x: isinstance(x, float) or isinstance(x, int)).all())

if __name__ == '__main__':
    unittest.main()
