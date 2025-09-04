


import folium
from flask import Blueprint, render_template, request
from markupsafe import Markup
from db_simulado import get_atracoes
import pandas as pd

mapa_bp = Blueprint('mapa', __name__)

@mapa_bp.route('/mapa')
def mapa():
        tipo_param = request.args.get('tipo')
        acess_param = request.args.get('acess')
        tipos = tipo_param.split(',') if tipo_param else []
        acesses = acess_param.split(',') if acess_param else []
        df = get_atracoes()
        dados = []
        for _, row in df.iterrows():
                acess_list = []
                if str(row.get("acessivel", "")).lower() == "true":
                        acess_list.append("mobilidade")
                if str(row.get("acess_visual", "")).lower() == "true":
                        acess_list.append("visual")
                if str(row.get("acess_auditiva", "")).lower() == "true":
                        acess_list.append("auditiva")
                if str(row.get("acess_outras", "")).lower() == "true":
                        acess_list.append("outras")
                dados.append({
                        "nome": row["nome"],
                        "tipo": row.get("tipo", "atracao"),
                        "acessibilidade": acess_list,
                        "lat": float(row["latitude"]),
                        "lng": float(row["longitude"]),
                        "cidade": row.get("cidade", ""),
                        "categoria": row.get("categoria", ""),
                        "destaque": bool(row.get("destaque", False)),
                })

        # Filtragem correta fora do loop
        dados_filtrados = dados
        if tipos:
                dados_filtrados = [p for p in dados_filtrados if p['tipo'] in tipos]
        if acesses:
                dados_filtrados = [p for p in dados_filtrados if any(a in p['acessibilidade'] for a in acesses)]

        # Centralização dinâmica se lat/lng na query
        lat = request.args.get('lat', type=float)
        lng = request.args.get('lng', type=float)
        zoom = request.args.get('zoom', type=int)
        center = [lat, lng] if lat and lng else [-11.5, 14]
        zoom_start = zoom if zoom else (13 if lat and lng else 5)
        m = folium.Map(location=center, zoom_start=zoom_start, tiles='OpenStreetMap')
        tipo_cores = {
                "hospedagem": "blue",
                "restaurante": "green",
                "atracao": "purple",
                "transporte": "orange",
        }
        for ponto in dados_filtrados:
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
