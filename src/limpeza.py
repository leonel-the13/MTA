import pandas as pd
import os

def limpar_csv(input_path, output_path, drop_duplicates=True):
    df = pd.read_csv(input_path)
    if drop_duplicates:
        df = df.drop_duplicates()
    df = df.fillna('')
    df.to_csv(output_path, index=False)
    print(f"Arquivo limpo salvo em: {output_path}")

if __name__ == "__main__":
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    arquivos = [
        'atracoes.csv',
        'visitantes.csv',
        'reservas.csv',
    ]
    for nome in arquivos:
        input_path = os.path.join(data_dir, nome)
        output_path = os.path.join(data_dir, f"limpo_{nome}")
        limpar_csv(input_path, output_path)