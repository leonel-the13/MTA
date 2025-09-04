import pandas as pd
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

def get_atracoes():
    return pd.read_csv(os.path.join(data_dir, 'atracoes.csv'), delimiter=',')

def get_visitantes():
    return pd.read_csv(os.path.join(data_dir, 'visitantes.csv'), delimiter=',')

def get_reservas():
    return pd.read_csv(os.path.join(data_dir, 'reservas.csv'), delimiter=',')

if __name__ == "__main__":
    print('Atrações:')
    print(get_atracoes().head())
    print('\nVisitantes:')
    print(get_visitantes().head())
    print('\nReservas:')
    print(get_reservas().head())
