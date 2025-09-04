import folium
from flask import Blueprint, render_template
from markupsafe import Markup
from db_simulado import get_atracoes

mapa_bp = Blueprint('mapa_bp', __name__)

@mapa_bp.route('/mapa_folium')
def mapa_folium():
        dados = get_atracoes()
        m = folium.Map(location=[-11.5, 14], zoom_start=6, control_scale=True, tiles='OpenStreetMap')
        for _, row in dados.iterrows():
                nome = row.get('nome', 'Atração')
                lat = float(row.get('latitude', 0))
                lon = float(row.get('longitude', 0))
                acess = row.get('acessivel', 'False')
                cor = 'green' if str(acess).lower() == 'true' else 'red'
                popup_html = f"""
                <div style='min-width:180px'>
                        <strong>{nome}</strong><br/>
                        <span style='color:{'green' if cor=='green' else 'red'};font-weight:bold;'>Acessível: {'Sim' if str(acess).lower()=='true' else 'Não'}</span><br/>
                        <span style='font-size:12px;'>Lat: {lat:.4f}, Lon: {lon:.4f}</span>
                </div>
                """
                folium.Marker(
                        [lat, lon],
                        popup=folium.Popup(popup_html, max_width=250),
                        icon=folium.Icon(color=cor, icon='info-sign')
                ).add_to(m)

        folium_html = m.get_root().render().replace('<body>', '').replace('</body>', '')
        folium_js = Markup(folium_html)

        lista_html = """
        <div class='overflow-y-auto' style='max-height:60vh;'>
                <h2 class='text-xl font-bold mb-4'>Atrações no Banco de Dados</h2>
                <ul class='space-y-4'>
        """
        if len(dados) == 0:
                lista_html += "<li class='text-gray-500'>Nenhuma atração cadastrada.</li>"
        else:
                for _, row in dados.iterrows():
                        nome = row.get('nome', 'Atração')
                        lat = float(row.get('latitude', 0))
                        lon = float(row.get('longitude', 0))
                        acess = row.get('acessivel', 'False')
                        cor = 'green' if str(acess).lower() == 'true' else 'red'
                        lista_html += f"""
                        <li class='bg-white rounded-lg shadow p-4 flex flex-col md:flex-row md:items-center md:justify-between'>
                                <div>
                                        <span class='font-semibold'>{nome}</span><br/>
                                        <span class='text-sm text-gray-600'>Lat: {lat:.4f}, Lon: {lon:.4f}</span>
                                </div>
                                <span class='inline-block mt-2 md:mt-0 px-3 py-1 rounded-full text-white' style='background:{cor};'>Acessível: {'Sim' if str(acess).lower()=='true' else 'Não'}</span>
                        </li>
                        """
        lista_html += """
                </ul>
        </div>
        """
        return render_template(
                'pages/mapa_folium_custom.html',
                folium_js=folium_js,
                lista_html=lista_html
        )
