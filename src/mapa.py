import folium
import pandas as pd
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
atracoes = pd.read_csv(os.path.join(data_dir, 'atracoes.csv'), delimiter='-')

m = folium.Map(location=[-11.5, 17.8], zoom_start=6)

for _, row in atracoes.iterrows():
    try:
        lat = float(row['latitude'])
        lon = float(row['longitude'])
        acessivel = row['acessivel'] == 'True'
        color = 'green' if acessivel else 'red'
        folium.Marker(
            location=[lat, lon],
            popup=f"<b>{row['nome']}</b><br>Acessível: {'Sim' if acessivel else 'Não'}",
            icon=folium.Icon(color=color)
        ).add_to(m)
    except Exception as e:
        print(f"Erro na linha: {row.to_dict()} - {e}")

output_path = os.path.join(data_dir, 'mapa_atracoes.html')
m.save(output_path)
print(f"Mapa salvo em {output_path}")

def mapa():
    print('logica de mapa')

if __name__ == "__main__":
    mapa()