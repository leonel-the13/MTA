import unittest
import os
import pandas as pd
from src import limpeza

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

class TestLimpeza(unittest.TestCase):
    def test_limpar_csv(self):
        input_path = os.path.join(data_dir, 'atracoes.csv')
        output_path = os.path.join(data_dir, 'test_limpo_atracoes.csv')
        limpeza.limpar_csv(input_path, output_path)
        self.assertTrue(os.path.exists(output_path))
        df = pd.read_csv(output_path)
        self.assertFalse(df.empty)
        os.remove(output_path)

if __name__ == '__main__':
    unittest.main()
