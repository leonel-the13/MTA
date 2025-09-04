import unittest
import os
from src import visualizacao

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

def test_graficos_existem():
    assert os.path.exists(os.path.join(data_dir, 'grafico_acessibilidade.png'))
    assert os.path.exists(os.path.join(data_dir, 'grafico_mais_visitadas.png'))

if __name__ == '__main__':
    test_graficos_existem()
    print('Testes de visualização OK')
