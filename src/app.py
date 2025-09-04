import logging
import sys
from flask import Flask, render_template, jsonify, send_from_directory
import pathlib
import os

from db_simulado import get_atracoes, get_visitantes, get_reservas
from mapa import mapa_bp
DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))



# Configuração de logging colorido
class AnsiColor:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

logging.basicConfig(
    level=logging.INFO,
    format=f'{AnsiColor.CYAN}[%(asctime)s]{AnsiColor.RESET} %(message)s',
    stream=sys.stdout
)

app = Flask(
    __name__,
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
)

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))


# Rota para servir arquivos da pasta data (gráficos, csvs, etc)
@app.route('/data/<path:filename>')
def data_files(filename):
    return send_from_directory(DATA_DIR, filename)

@app.route('/')
def index():
    logging.info(f'{AnsiColor.GREEN}Página inicial acessada{AnsiColor.RESET}')
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('pages/sobre.html')

@app.route('/destinos')
def destinos():
    logging.info(f'{AnsiColor.YELLOW}Página de destinos acessada{AnsiColor.RESET}')
    return render_template('pages/destinos.html')

@app.route('/contato')
def contato():
    return render_template('pages/contato.html')

@app.route('/api/atracoes')
def api_atracoes():
    logging.info(f'{AnsiColor.CYAN}API /api/atracoes chamada{AnsiColor.RESET}')
    dados = get_atracoes()
    # Seleciona apenas as colunas relevantes e remove duplicatas
    colunas = ['nome', 'latitude', 'longitude']
    dados = dados[colunas].drop_duplicates()
    logging.info(f'{AnsiColor.GREEN}API retornou {len(dados)} atrações{AnsiColor.RESET}')
    return jsonify(dados.to_dict(orient="records"))

@app.route('/api/visitantes')
def api_visitantes():
    dados = get_visitantes()
    dados = dados.rename(columns={
        'id_visitante': 'id',
        'nome': 'nome',
        'atracao': 'atracao',
        'mes': 'mes'
    })
    return jsonify(dados.to_dict(orient='records'))

@app.route('/api/reservas')
def api_reservas():
    dados = get_reservas()
    dados = dados.rename(columns={
        'id_reserva': 'id',
        'hotel': 'hotel',
        'cidade': 'cidade',
        'acessivel': 'acessivel',
        'noites': 'noites',
        'hospedes': 'hospedes',
        'mes': 'mes'
    })
    return jsonify(dados.to_dict(orient='records'))

app.register_blueprint(mapa_bp)

if __name__ == '__main__':
    app.run(debug=True)
