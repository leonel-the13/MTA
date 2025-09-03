from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(
    __name__,
    template_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates')),
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
)

def load_data():
    return pd.read_csv('data/atracoes.csv')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/atracoes')
def api_atracoes():
    dados = load_data()
    return jsonify(dados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
