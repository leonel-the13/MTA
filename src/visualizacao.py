import pandas as pd
import matplotlib.pyplot as plt
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

# Carregar dados reais
atracoes = pd.read_csv(os.path.join(data_dir, 'atracoes.csv'), delimiter=',')
visitantes = pd.read_csv(os.path.join(data_dir, 'visitantes.csv'), delimiter=',')
reservas = pd.read_csv(os.path.join(data_dir, 'reservas.csv'), delimiter=',')

# KPI 1: Total de atrações acessíveis
kpi_acessiveis = atracoes['acessivel'].astype(str).str.strip().str.lower().eq('true').sum()
print(f"Atrações totalmente acessíveis: {kpi_acessiveis}")

# KPI 2: Total de reservas em hotéis acessíveis
kpi_reservas_acessiveis = reservas['acessivel'].astype(str).str.strip().str.lower().eq('true').sum()
print(f"Reservas em hotéis acessíveis: {kpi_reservas_acessiveis}")

# Gráfico de barras: Acessibilidade das atrações
plt.figure(figsize=(6,4))
atracoes['acessivel'].replace({'True': 'Sim', 'False': 'Não'}).value_counts().plot(kind='bar', color=['#22c55e', '#ef4444'])
plt.title('Acessibilidade das Atrações')
plt.xlabel('Acessível')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_acessibilidade.png'))
plt.close()

# Gráfico de pizza: Atrações mais visitadas
plt.figure(figsize=(6,6))
visitantes['atracao'].value_counts().head(6).plot(kind='pie', autopct='%1.1f%%')
plt.title('Atrações Mais Visitadas')
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_mais_visitadas.png'))
plt.close()

print('Gráficos salvos em data/.')

def visualizacao():
    print('logica de visualizacao de dados')

if __name__ == "__main__":
    visualizacao()