import pandas as pd
import matplotlib.pyplot as plt
import os

data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')

atracoes = pd.read_csv(os.path.join(data_dir, 'atracoes.csv'), delimiter=',')
visitantes = pd.read_csv(os.path.join(data_dir, 'visitantes.csv'), delimiter=',')
reservas = pd.read_csv(os.path.join(data_dir, 'reservas.csv'), delimiter=',')

kpi_acessiveis = atracoes['acessivel'].astype(str).str.strip().str.lower().eq('true').sum()
print(f"Atrações totalmente acessíveis: {kpi_acessiveis}")

kpi_reservas_acessiveis = reservas['acessivel'].astype(str).str.strip().str.lower().eq('true').sum()
print(f"Reservas em hotéis acessíveis: {kpi_reservas_acessiveis}")

plt.figure(figsize=(6,4))
atracoes['acessivel'].replace({'True': 'Sim', 'False': 'Não'}).value_counts().plot(kind='bar', color=['#22c55e', '#ef4444'])
plt.title('Acessibilidade das Atrações')
plt.xlabel('Acessível')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_acessibilidade.png'))
plt.close()

plt.figure(figsize=(6,6))
visitantes['atracao'].value_counts().head(6).plot(kind='pie', autopct='%1.1f%%')
plt.title('Atrações Mais Visitadas')
plt.ylabel('')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_mais_visitadas.png'))
plt.close()

# Top 10 atrações mais visitadas com info de acessibilidade
top10 = visitantes['atracao'].value_counts().head(10).reset_index()
top10.columns = ['atracao', 'visitas']
top10 = top10.merge(atracoes[['nome', 'acessivel']], left_on='atracao', right_on='nome', how='left')

plt.figure(figsize=(8,5))
colors = top10['acessivel'].replace({True: '#22c55e', False: '#ef4444'})
plt.bar(top10['atracao'], top10['visitas'], color=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Atrações Mais Visitadas (com acessibilidade)')
plt.xlabel('Atração')
plt.ylabel('Número de visitas')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_top10_acessibilidade.png'))
plt.close()

# Distribuição mensal de visitas
plt.figure(figsize=(8,5))
visitantes['mes'].value_counts().sort_index().plot(kind='bar')
plt.title('Distribuição Mensal de Visitas')
plt.xlabel('Mês')
plt.ylabel('Número de visitas')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_visitas_mensais.png'))
plt.close()


# 1. Reservas em hotéis acessíveis vs não acessíveis
plt.figure(figsize=(6,4))
reservas['acessivel'] = reservas['acessivel'].astype(str).str.strip().str.lower()
reservas['acessivel'].replace({'true': 'Acessível', 'false': 'Não Acessível'}, inplace=True)
reservas['acessivel'].value_counts().plot(kind='bar', color=['#22c55e', '#ef4444'])
plt.title('Reservas em Hotéis Acessíveis vs Não Acessíveis')
plt.xlabel('Tipo de Hotel')
plt.ylabel('Número de Reservas')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_reservas_acessibilidade.png'))
plt.close()


# 3. Visitantes em atrações acessíveis vs não acessíveis
plt.figure(figsize=(6,4))
visitantes_acess = visitantes.merge(atracoes[['nome', 'acessivel']], left_on='atracao', right_on='nome', how='left')
visitantes_acess['acessivel'] = visitantes_acess['acessivel'].astype(str).str.strip().str.lower()
visitantes_acess['acessivel'].replace({'true': 'Acessível', 'false': 'Não Acessível'}, inplace=True)
visitantes_acess['acessivel'].value_counts().plot(kind='bar', color=['#16a34a', '#dc2626'])
plt.title('Visitantes em Atrações Acessíveis vs Não Acessíveis')
plt.xlabel('Acessibilidade')
plt.ylabel('Número de Visitantes')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_visitantes_acessibilidade.png'))
plt.close()

# 4. Linha temporal de visitas em atrações acessíveis vs não acessíveis
plt.figure(figsize=(8,5))
visitantes_acess.groupby(['mes', 'acessivel']).size().unstack().plot(kind='line', marker='o')
plt.title('Visitas Mensais: Atrações Acessíveis vs Não Acessíveis')
plt.xlabel('Mês')
plt.ylabel('Número de Visitas')
plt.legend(title='Acessibilidade')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_visitas_mensais.png'))
plt.close()

# Gráfico: Tipos de Acessibilidade mais comuns nas atrações
plt.figure(figsize=(7,5))

# Quebrar os tipos múltiplos (ex.: "mobilidade|visual")
acess_tipos = atracoes['acessibilidade'].dropna().str.split('|').explode()

# Contar quantos de cada
acess_tipos.value_counts().plot(kind='bar', color='#3b82f6')

plt.title('Tipos de Acessibilidade Mais Comuns nas Atrações')
plt.xlabel('Tipo de Acessibilidade')
plt.ylabel('Número de Atrações')
plt.tight_layout()
plt.savefig(os.path.join(data_dir, 'grafico_tipos_acessibilidade.png'))
plt.close()

print("Gráfico salvo em data/grafico_tipos_acessibilidade.png")


print('Gráficos salvos em data/.')

def visualizacao():
    print('logica de visualizacao de dados')

if __name__ == "__main__":
    visualizacao()