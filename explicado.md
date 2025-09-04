# Explicação Detalhada do Projeto: Mapa de Turismo Acessível

## Objetivo

O projeto "Mapa de Turismo Acessível" visa mapear atrações turísticas e estabelecimentos com acessibilidade em Angola, facilitando o planejamento de viagens para pessoas com deficiência e promovendo o turismo sustentável e inclusivo.

## Funcionalidades

- Visualização de atrações acessíveis em um mapa interativo (Folium)
- Filtros dinâmicos por tipo de atração e acessibilidade
- Busca com autocomplete e centralização do mapa
- KPIs dinâmicos de turismo acessível
- Interface web responsiva com navegação unificada
- Backend robusto com Flask e API para dados
- Testes automatizados para backend, scripts e visualizações

## Estrutura do Projeto

```
MTA/
├── data/                # Dados CSV reais
│   └── atracoes.csv     # Base de dados principal
├── src/                 # Código-fonte Python
│   ├── app.py           # Backend Flask
│   ├── mapa.py          # Geração do mapa e filtros
│   ├── limpeza.py       # Limpeza e tratamento de dados
│   ├── visualizacao.py  # Gráficos e KPIs
│   └── db_simulado.py   # Leitura dos dados
├── templates/           # HTML (Jinja2)
│   ├── index.html
│   └── pages/
│       └── mapa.html
├── static/              # CSS e JS
│   ├── styles/
│   └── scripts/
├── requirements.txt     # Dependências
├── Makefile             # Comandos automatizados
└── README.md            # Documentação principal
```

## Bibliotecas Usadas

- **Flask**: Backend web e API
- **pandas**: Leitura, limpeza e manipulação de dados
- **folium**: Geração do mapa interativo
- **matplotlib**: Gráficos e visualizações
- **seaborn**: Visualização estatística (opcional, para gráficos avançados)

### Conferência das Bibliotecas do requirements.txt

- pandas: Usada em todos os scripts de dados
- matplotlib: Usada em visualizacao.py
- seaborn: Usada em visualizacao.py (opcional, mas importada)
- folium: Usada em mapa.py
- flask: Usada em app.py

**Todas as bibliotecas listadas em requirements.txt são utilizadas no projeto.**

## Detalhes Técnicos

- O backend Flask serve as páginas e a API de dados (através de rotas /api/atracoes, etc).
- O mapa é gerado dinamicamente com Folium, usando dados reais do CSV.
- Filtros e busca são implementados em JavaScript, consumindo endpoints Flask.
- O layout é responsivo, com navegação unificada (navbar igual em todas as telas).
- Testes automatizados cobrem rotas, scripts de dados e visualizações.

## Observações sobre a Navbar

- A navbar foi padronizada para ser idêntica em todas as telas, incluindo menu mobile.
- Caso note diferença visual, limpe o cache do navegador e recarregue as páginas.

## Como Executar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
2. Rode o backend:
   ```sh
   make run
   ```
3. Acesse http://127.0.0.1:5000 no navegador.

## Como Rodar os Testes

```sh
make test
```

## Contato

Dúvidas ou sugestões? Abra uma issue no repositório ou entre em contato com a equipe.
