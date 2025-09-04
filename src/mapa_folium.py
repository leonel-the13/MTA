import folium
from flask import Blueprint, render_template_string
from db_simulado import get_atracoes

mapa_bp = Blueprint('mapa_bp', __name__)

@mapa_bp.route('/mapa_folium')
def mapa_folium():
    dados = get_atracoes()
    m = folium.Map(location=[-8.8383, 13.2344], zoom_start=6)
    for _, row in dados.iterrows():
        nome = row.get('nome', 'Atração')
        lat = float(row.get('latitude', 0))
        lon = float(row.get('longitude', 0))
        acess = row.get('acessivel', 'False')
        cor = 'green' if str(acess).lower() == 'true' else 'red'
        folium.Marker(
            [lat, lon],
            popup=nome,
            icon=folium.Icon(color=cor)
        ).add_to(m)
        return render_template_string("""
        <!DOCTYPE html>
        <html lang='pt-BR'>
        <head>
                <meta charset='UTF-8'>
                <meta name='viewport' content='width=device-width, initial-scale=1.0'>
                <title>Mapa Folium - Turismo Acessível</title>
                <script src='https://cdn.tailwindcss.com'></script>
                <link href='https://unpkg.com/aos@2.3.1/dist/aos.css' rel='stylesheet' />
                <script src='https://unpkg.com/aos@2.3.1/dist/aos.js'></script>
                <script src='https://unpkg.com/feather-icons'></script>
                <script src='https://cdn.jsdelivr.net/npm/feather-icons/dist/feather.min.js'></script>
                <style>
                        .gradient-bg {background: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);}
                        /* Garante altura do mapa Folium */
                        #map {min-height: 50vh !important; height: 50vh !important;}
                        .folium-map {min-height: 50vh !important; height: 50vh !important;}
                </style>
        </head>
        <body class='bg-gray-50 font-sans'>
                <nav class='gradient-bg text-white shadow-lg'>
                        <div class='container mx-auto px-4 py-4 flex justify-between items-center'>
                                <div class='flex items-center space-x-2'>
                                        <i data-feather='map' class='w-8 h-8'></i>
                                        <span class='text-xl font-bold'>Turismo Acessível</span>
                                </div>
                                <div class='hidden md:flex space-x-6'>
                                        <a href='/' class='hover:text-blue-200 transition'>Início</a>
                                        <a href='/mapa_folium' class='text-blue-200 font-semibold'>Mapa</a>
                                        <a href='/destinos' class='hover:text-blue-200 transition'>Destinos</a>
                                        <a href='/sobre' class='hover:text-blue-200 transition'>Sobre Nós</a>
                                        <a href='/contato' class='hover:text-blue-200 transition'>Contato</a>
                                </div>
                                <button class='md:hidden' id='menu-btn'>
                                    <i data-feather='menu' class='w-6 h-6'></i>
                                </button>
                        </div>
                        <!-- Mobile Menu -->
                        <div class='md:hidden hidden px-4 pb-4' id='mobile-menu'>
                            <a href='/' class='block py-2 hover:text-blue-200'>Início</a>
                            <a href='/mapa_folium' class='block py-2 hover:text-blue-200'>Mapa</a>
                            <a href='/destinos' class='block py-2 hover:text-blue-200'>Destinos</a>
                            <a href='/sobre' class='block py-2 hover:text-blue-200'>Sobre Nós</a>
                            <a href='/contato' class='block py-2 hover:text-blue-200'>Contato</a>
                        </div>
                </nav>
                <section class='pt-10 pb-6 bg-white'>
                        <div class='container mx-auto px-4'>
                                <h1 class='text-3xl font-bold mb-6 text-center'>Mapa de Acessibilidade (Folium)</h1>
                                <div class='rounded-lg shadow-lg mb-8' style='overflow:hidden; min-height:50vh;'>
                                        {{ mapa_html|safe }}
                                </div>
                        </div>
                </section>
                <script>
                    AOS.init({duration:800,easing:'ease-in-out',once:true});
                    feather.replace();
                    document.getElementById('menu-btn').addEventListener('click', function () {
                        const menu = document.getElementById('mobile-menu');
                        if (menu.classList.contains('hidden')) {
                            menu.classList.remove('hidden');
                            feather.replace();
                        } else {
                            menu.classList.add('hidden');
                        }
                    });
                </script>
        </body>
        </html>
        """, mapa_html=m._repr_html_())
