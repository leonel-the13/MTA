


import folium
from flask import Blueprint, render_template, request
from markupsafe import Markup
from db_simulado import get_atracoes
import pandas as pd

mapa_bp = Blueprint('mapa', __name__)

@mapa_bp.route('/mapa')
def mapa():
        tipo = request.args.get('tipo')
        acess = request.args.get('acess')
        df = get_atracoes()
        dados = []
        for _, row in df.iterrows():
                dados.append({
                        "nome": row["nome"],
                        "tipo": row.get("tipo", "atracao"),
                        "acessibilidade": ["mobilidade"] if str(row["acessivel"]).lower() == "true" else [],
                        "lat": float(row["latitude"]),
                        "lng": float(row["longitude"]),
                        "cidade": row.get("cidade", ""),
                        "categoria": row.get("categoria", ""),
                        "destaque": bool(row.get("destaque", False)),
                })

        if tipo:
                dados = [p for p in dados if p['tipo'] == tipo]
        if acess:
                dados = [p for p in dados if acess in p['acessibilidade']]

        m = folium.Map(location=[-11.5, 14], zoom_start=6, tiles='OpenStreetMap')
        tipo_cores = {
                "hospedagem": "blue",
                "restaurante": "green",
                "atracao": "purple",
                "transporte": "orange",
        }
        for ponto in dados:
                cor = tipo_cores.get(ponto["tipo"], "gray")
                popup_html = f"""
                <div style='min-width:180px'>
                        <strong>{ponto['nome']}</strong><br/>
                        <span style='color: {cor}; font-weight: bold;'>Tipo: {ponto['tipo'].capitalize()}</span><br/>
                        <span style='font-size:12px;'>Acessibilidade: {', '.join(ponto['acessibilidade']) if ponto['acessibilidade'] else 'Não acessível'}</span>
                </div>
                """
                folium.Marker(
                                [ponto["lat"], ponto["lng"]],
                                popup=folium.Popup(popup_html, max_width=250),
                                icon=folium.Icon(color=cor, icon='info-sign')
                        ).add_to(m)

        folium_html = m.get_root().render().replace('<body>', '').replace('</body>', '')
        folium_map = Markup(folium_html)
        return render_template('pages/mapa.html', folium_map=folium_map)
