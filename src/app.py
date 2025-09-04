from flask import Flask, render_template, jsonify
import os

from db_simulado import get_atracoes, get_visitantes, get_reservas
from mapa_folium import mapa_bp

app = Flask(
    __name__,
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
)

@app.route('/')
def index():
    return render_template('index.html')

from flask import redirect, url_for

@app.route('/mapa')
def mapa():
    return redirect(url_for('mapa_bp.mapa_folium'))

@app.route('/sobre')
def sobre():
    return render_template('pages/sobre.html')

@app.route('/contato')
def contato():
    return render_template('pages/contato.html')

@app.route('/destinos')
def destinos():
    return render_template('pages/destinos.html')

@app.route('/api/atracoes')
def api_atracoes():
    dados = get_atracoes()
    # Renomear colunas para frontend
    dados = dados.rename(columns={
        'nome': 'nome',
        'latitude': 'latitude',
        'longitude': 'longitude',
        'acessivel': 'acessibilidade'
    })
    # Adicionar campos fictícios para cidade, endereco e tipo
    cidades = [
        "Luanda", "Benguela", "Huíla", "Malanje", "Namibe", "Huambo", "Cuanza Sul", "Bengo", "Zaire", "Cuando Cubango"
    ]
    tipos = [
        "Praia", "Museu", "Parque", "Miradouro", "Cachoeira", "Monumento", "Serra"
    ]
    enderecos = [
        "Centro", "Zona Turística", "Avenida Principal", "Bairro Antigo", "Marginal", "Próximo ao Rio", "Estrada Nacional"
    ]
    import random
    dados["cidade"] = [random.choice(cidades) for _ in range(len(dados))]
    dados["tipo"] = [random.choice(tipos) for _ in range(len(dados))]
    dados["endereco"] = [random.choice(enderecos) for _ in range(len(dados))]
    return jsonify(dados.to_dict(orient='records'))

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
