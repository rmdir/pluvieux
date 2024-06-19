from django.urls import path
from .views import index
from .views import Cartes
from .views import Statistiques
from .views import mapview
from .views import precipitation
from .views import temperature
from .views import ndvi
from .views import pressure

urlpatterns = [
    path('index/', index, name="index"),
    path('Cartes/', Cartes, name='Cartes'),
    path('Statistiques/', Statistiques, name='Statistiques'),
    path('map/', mapview, name='Map'),
    path('Cartes/map_precipitation.html', precipitation),
    path('Cartes/map_ndvi.html', ndvi),
    path('Cartes/map_temperature.html', temperature),
    path('Cartes/map_pressure.html', pressure)
]
