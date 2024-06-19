import ee
import folium
from folium.elements import *
from datetime import timedelta, datetime
import branca
from jinja2 import Template
from folium import plugins


ee.Authenticate()
ee.Initialize(project='ee-baptistebarraque')

collections = {'NDVI': 'MODIS/061/MOD13A1',
               'else': 'ECMWF/ERA5_LAND/DAILY_AGGR'}

bands = {'Rainfall': 'total_precipitation_max',
         'Pressure': 'surface_pressure_max', 'Evaporation': 'total_evaporation_max', 'Temperature': 'temperature_2m'}


def map_ndvi(date_t):

    date = datetime.strptime(date_t, '%Y-%m-%d')

# Ajouter un jour à la date
    next_date = date + timedelta(days=30)

# Convertir la date suivante en format de chaîne de caractères 'YYYY-MM-DD'
    next_date_str = next_date.strftime('%Y-%m-%d')
    dataset = ee.ImageCollection(
        'MODIS/061/MOD13A1').filter(ee.Filter.date(date_t, next_date_str))
    ndvi = dataset.select('NDVI')
    ndviVis = {
        'min': 0,
        'max': 9000,
        'palette': [
            'ffffff', 'ce7e45', 'df923d', 'f1b555', 'fcd163', '99b718', '74a901',
            '66a000', '529400', '3e8601', '207401', '056201', '004c00', '023b01',
            '012e01', '011d01', '011301'

        ],
        'opacity': 0.6
    }
    m = folium.Map(location=[46.529, 6.746], zoom_start=2)
    folium.TileLayer(
        tiles=ndvi.getMapId(ndviVis)['tile_fetcher'].url_format,
        attr='NDVI',
        overlay=True,
        name='NDVI'
    ).add_to(m)
    m.save('C:/Users/Baptiste/OneDrive/Documents/Centrale/Projet/projet-900M2/DocBlog/src/blog/templates/blog/maps/map_ndvi.html')


def map_temperature(date_t):

    date = datetime.strptime(date_t, '%Y-%m-%d')

# Ajouter un jour à la date
    next_date = date + timedelta(days=1)

# Convertir la date suivante en format de chaîne de caractères 'YYYY-MM-DD'
    next_date_str = next_date.strftime('%Y-%m-%d')
    dataset = ee.ImageCollection(
        'ECMWF/ERA5_LAND/DAILY_AGGR').filter(ee.Filter.date(date_t, next_date_str))
    ndvi = dataset.select('temperature_2m')
    Vis = {
        'min': 250,
        'max': 320,
        'palette': [
            '000080', '0000d9', '4000ff', '8000ff', '0080ff', '00ffff',
            '00ff80', '80ff00', 'daff00', 'ffff00', 'fff500', 'ffda00',
            'ffb000', 'ffa400', 'ff4f00', 'ff2500', 'ff0a00', 'ff00ff'
        ], 'opacity': 0.7
    }
    m = folium.Map(location=[46.529, 6.746], zoom_start=2)
    folium.TileLayer(
        tiles=ndvi.getMapId(Vis)['tile_fetcher'].url_format,
        attr='Temperature',
        overlay=True,
        name='Temperature',

    ).add_to(m)
    m.save('C:/Users/Baptiste/OneDrive/Documents/Centrale/Projet/projet-900M2/DocBlog/src/blog/templates/blog/maps/map_temperature.html')


def map_pressure(date_t):

    date = datetime.strptime(date_t, '%Y-%m-%d')

# Ajouter un jour à la date
    next_date = date + timedelta(days=1)

# Convertir la date suivante en format de chaîne de caractères 'YYYY-MM-DD'
    next_date_str = next_date.strftime('%Y-%m-%d')
    dataset = ee.ImageCollection(
        'ECMWF/ERA5_LAND/DAILY_AGGR').filter(ee.Filter.date(date_t, next_date_str))
    pressure = dataset.select('surface_pressure')
    pressureVis = {
        'min': 90000,
        'max': 103500,
        'palette': [
            '#0000ff', '#0000ff', '#0000ff',  # Bleu foncé pour les pressions très basses
            '#0000ff', '#4169e1', '#6495ed',  # Bleu pour les pressions basses
            '#87ceeb', '#add8e6', '#b0e0e6',  # Bleu clair pour les pressions modérées
            '#f0f8ff', '#ffe4b5', '#ffd700',  # Jaune pour les pressions moyennes
            '#ffd700', '#ffd700', '#ffd700',  # Jaune pour les pressions moyennes
            '#ffa500', '#ff7f50', '#ff6347',  # Orange pour les pressions élevées
            '#ff4500', '#ff4500', '#ff4500',  # Rouge pour les pressions très élevées
            '#ff0000', '#ff0000', '#ff0000'

        ],
        'opacity': 0.7
    }
    m = folium.Map(location=[46.529, 6.746],
                   zoom_start=2)
    folium.TileLayer(
        tiles=pressure.getMapId(pressureVis)['tile_fetcher'].url_format,
        attr='Pressure',
        overlay=True,
        name='Pressure'
    ).add_to(m)
    m.save('C:/Users/Baptiste/OneDrive/Documents/Centrale/Projet/projet-900M2/DocBlog/src/blog/templates/blog/maps/map_pressure.html')


def map_precipitation(date_t):

    date = datetime.strptime(date_t, '%Y-%m-%d')

# Ajouter un jour à la date
    next_date = date + timedelta(days=1)

# Convertir la date suivante en format de chaîne de caractères 'YYYY-MM-DD'
    next_date_str = next_date.strftime('%Y-%m-%d')
    dataset = ee.ImageCollection(
        'ECMWF/ERA5_LAND/DAILY_AGGR').filter(ee.Filter.date(date_t, next_date_str))
    precipitation = dataset.select('total_precipitation_max')
    precipitationVis = {
        'min': 0,
        'max': 0.007,
        'palette': [
            'ffffff', '00ffff', '0080ff', 'da00ff', 'ffa400', 'ff0000'

        ],
        'opacity': 0.6
    }
    m = folium.Map(location=[46.529, 6.746], zoom_start=2)
    folium.TileLayer(
        tiles=precipitation.getMapId(precipitationVis)[
            'tile_fetcher'].url_format,
        attr='Precipitation',
        overlay=True,
        name='Precipitation'
    ).add_to(m)
    m.save('C:/Users/Baptiste/OneDrive/Documents/Centrale/Projet/projet-900M2/DocBlog/src/blog/templates/blog/maps/map_precipitation.html')


# Cette fonction charge indivuduellement les différentes cartes pour chaque donnée.

def map_global(date_t):

    # Cartes superposant une seule donnée à la fois
    map_ndvi(date_t)
    map_precipitation(date_t)
    map_temperature(date_t)
    map_pressure(date_t)

# Fonction qui permet de générer la légende


def add_gradient_legend(map_obj, title, min_value, max_value, colors, unit, margin):
    position_styles = {
        'topright': f'top: {50 + margin}px; right: 50px;',
        'bottomright': f'bottom: {50 + margin}px; right: 50px;',
        'topleft': f'top: {50 + margin}px; left: 50px;',
        'bottomleft': f'bottom: {50 + margin}px; left: 50px;'
    }

    position_style = position_styles.get('bottomright')
    print(position_style)
    gradient = "background: linear-gradient(to right, " + \
        ', '.join(colors) + ");"

    legend_html = f'''
        <div style="position: fixed; {position_style} width: 300px; height: 70px; 
                    background-color: white; border: 2px solid grey; z-index: 9999; font-size: 14px;">
            <div style="padding: 5px 10px; font-weight: bold;">{title}</div>
            <div style="height: 10px; {gradient}"></div>
            <div style="display: flex; justify-content: space-between; padding: 0 10px;">
                <span>{min_value} {unit}</span>
                <span>{max_value} {unit}</span>
            </div>
        </div>
    '''

    map_obj.get_root().html.add_child(folium.Element(legend_html))

# Fonction qui définit les sliders d'opacité:


def html_opacity_slider(parameters):
    sliders_html = '''<div class=opacity-slider>'''
    scripts_html = '''<script>

        var sliders = document.querySelectorAll('.slider');
        var tileLayers = document.querySelectorAll('.leaflet-tile-pane > .leaflet-layer');

        sliders.forEach(function (slider, index) {
            slider.addEventListener('input', function (e) {
                tileLayers[index + 1].style.opacity = e.target.value;
            });
        });
        </script>'''

    for index, param in enumerate(parameters, start=1):
        sliders_html += f'''
        <label for="opacity{index}">Opacité de la carte {param}:</label>
        <input type="range" id="opacity{index}" class="slider" min="0" max="1" step="0.1" value="1">
        <br>'''

    sliders_html += f'''</div>'''
    style_html = '''
    <style>
        .opacity-slider {
            position: absolute;
            bottom: 10px;
            left: 10px;
            z-index: 1000;
            background: white;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
            font-family: 'Arial', sans-serif;
        }
        .slider {
            -webkit-appearance: none;
            width: 100%;
            height: 10px;
            background: linear-gradient(to right, #4CAF50, #F44336);
            outline: none;
            border-radius: 5px;
            transition: background 0.3s ease-in-out;
        }
        .slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            background: #4CAF50;
            cursor: pointer;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            transition: background 0.3s ease-in-out, transform 0.2s;
        }
        .slider::-webkit-slider-thumb:hover {
            background: #3E8E41;
            transform: scale(1.2);
        }
        .slider::-moz-range-thumb {
            width: 20px;
            height: 20px;
            background: #4CAF50;
            cursor: pointer;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
            transition: background 0.3s ease-in-out, transform 0.2s;
        }
        .slider::-moz-range-thumb:hover {
            background: #3E8E41;
            transform: scale(1.2);
        }
        .slider-label {
            font-size: 14px;
            margin-bottom: 5px;
            color: #333;
        }
    </style>'''
    html_dico = {'div': sliders_html+style_html,
                 'script': scripts_html}
    return html_dico


def dynamic_superposition(date_t, parameter_list):
    date = datetime.strptime(date_t, '%Y-%m-%d')

# Ajouter un jour à la date
    next_date = date + timedelta(days=1)
    next_date1 = date+timedelta(days=30)

# Convertir la date suivante en format de chaîne de caractères 'YYYY-MM-DD'
    next_date_str = next_date.strftime('%Y-%m-%d')
    next_date_str1 = next_date1.strftime('%Y-%m-%d')
    m = folium.Map(location=[46.529, 6.746],
                   zoom_start=2, tiles="Cartodb Positron")

    # Bases de données de travail
    dataset1 = ee.ImageCollection(
        'MODIS/061/MOD13A1').filter(ee.Filter.date(date_t, next_date_str1))
    dataset2 = ee.ImageCollection(
        'ECMWF/ERA5_LAND/DAILY_AGGR').filter(ee.Filter.date(date_t, next_date_str))
    margin_top = 0
    html_dico = html_opacity_slider(parameter_list)
    html_script = folium.Element(html_dico['script'])

    html_div = html_dico['div']
    m.get_root().html.add_child(folium.Element(html_div))
    m.get_root().html.add_child(html_script, name='script')
    for parameter in parameter_list:

        if parameter == 'Indice de végétation':
            ndvi = dataset1.select('NDVI')
            ndviVis = {
                'min': 0,
                'max': 9000,
                'palette': [
                    'ffffff', 'ce7e45', 'df923d', 'f1b555', 'fcd163', '99b718', '74a901',
                    '66a000', '529400', '3e8601', '207401', '056201', '004c00', '023b01',
                    '012e01', '011d01', '011301'

                ],
                'opacity': 0.7
            }
            ndvi_url = ndvi.getMapId(ndviVis)['tile_fetcher'].url_format
            ndvi_tile_layer = folium.TileLayer(
                tiles=ndvi.getMapId(ndviVis)['tile_fetcher'].url_format,
                attr='NDVI',
                overlay=True,
                name='NDVI',

            ).add_to(m)
            ndvi_colors = []
            for color in ndviVis['palette']:
                ndvi_colors.append('#'+color)

            add_gradient_legend(m, 'Indice de végétation',
                                0, 9000, ndvi_colors, " ", margin_top)
            margin_top += 70

        if parameter == 'Température':
            temperatureVis = {
                'min': 250,
                'max': 320,
                'palette': [
                    '000080', '0000d9', '4000ff', '8000ff', '0080ff', '00ffff',
                    '00ff80', '80ff00', 'daff00', 'ffff00', 'fff500', 'ffda00',
                    'ffb000', 'ffa400', 'ff4f00', 'ff2500', 'ff0a00', 'ff00ff'
                ], 'opacity': 0.6
            }
            temperature = dataset2.select('temperature_2m')
            folium.TileLayer(
                tiles=temperature.getMapId(temperatureVis)[
                    'tile_fetcher'].url_format,
                attr='Temperature',
                overlay=True,
                name='Temperature',
            ).add_to(m)
            temp_colors = []
            for color in temperatureVis['palette']:
                temp_colors.append('#'+color)
            add_gradient_legend(m, 'Température',
                                250, 320, temp_colors, 'Kelvin', margin_top)
            margin_top += 70
        if parameter == 'Pression':
            pressure = dataset2.select('surface_pressure')
            pressureVis = {
                'min': 90000,
                'max': 103500,
                'palette': [
                    '#0000ff', '#0000ff', '#0000ff',  # Bleu foncé pour les pressions très basses
                    '#0000ff', '#4169e1', '#6495ed',  # Bleu pour les pressions basses
                    '#87ceeb', '#add8e6', '#b0e0e6',  # Bleu clair pour les pressions modérées
                    '#f0f8ff', '#ffe4b5', '#ffd700',  # Jaune pour les pressions moyennes
                    '#ffd700', '#ffd700', '#ffd700',  # Jaune pour les pressions moyennes
                    '#ffa500', '#ff7f50', '#ff6347',  # Orange pour les pressions élevées
                    '#ff4500', '#ff4500', '#ff4500',  # Rouge pour les pressions très élevées
                    '#ff0000', '#ff0000', '#ff0000'

                ],
                'opacity': 0.6
            }

            folium.TileLayer(
                tiles=pressure.getMapId(pressureVis)[
                    'tile_fetcher'].url_format,
                attr='Pressure',
                overlay=True,
                name='Pressure'
            ).add_to(m)
            pressure_colors = []
            for color in pressureVis['palette']:
                # Les # sont déjà mis dans la palette
                pressure_colors.append(color)
            add_gradient_legend(m, 'Pression',
                                90000, 103500, pressure_colors, 'hPa', margin_top)
            margin_top += 70

        if parameter == 'Précipitations':
            precipitation = dataset2.select('total_precipitation_max')
            precipitationVis = {
                'min': 0,
                'max': 0.007,
                'palette': [
                    'ffffff', '00ffff', '0080ff', 'da00ff', 'ffa400', 'ff0000'

                ],
                'opacity': 0.6
            }

            folium.TileLayer(
                tiles=precipitation.getMapId(precipitationVis)[
                    'tile_fetcher'].url_format,
                attr='Precipitation',
                overlay=True,
                name='Precipitation'
            ).add_to(m)
            precipitation_colors = []
            for color in precipitationVis['palette']:
                precipitation_colors.append('#'+color)
            add_gradient_legend(m, 'Précipitations',
                                0, 0.2, precipitation_colors, 'm', margin_top)
            margin_top += 70

    folium.LayerControl().add_to(m)

    folium.plugins.Fullscreen(
        position="topright",
        title="Expand me",
        title_cancel="Exit me",
        force_separate_button=True,
    ).add_to(m)

    # Permet de rentrer une localisation
    folium.plugins.Geocoder().add_to(m)
    # Accède directement à la localisation de l'utilisateur
    folium.plugins.LocateControl(initialZoomLevel=2).add_to(m)
    m.save('C:/Users/Baptiste/OneDrive/Documents/Centrale/Projet/projet-900M2/DocBlog/src/blog/templates/blog/maps/map_dynamic_superposition.html')
