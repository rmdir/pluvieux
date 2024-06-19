import requests
import time
from datetime import datetime, timedelta
import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils.map import map_global
from .utils.map import dynamic_superposition
from django.http import JsonResponse
from .models import Event
from .forms import FormulaireCarte
from django.contrib import messages


def index(request):
    print("ok")
    return render(request, "blog/index.html")


def Statistiques(request):
    return render(request, "blog/Statistiques.html")


def Cartes(request):
    page_carte = "/blog/empty"

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = FormulaireCarte(request.POST)
        if form.is_valid():

            # toutes les différentes pages html se mettent à jour
            parameters = request.POST.getlist('form-0-choix_data')
            if 'Cartes Séparées' in parameters and len(parameters) > 1:
                messages.error(
                    request, "Si vous sélectionnez l'option Cartes Séparées, veillez à sélectionner uniquement cette case")
                context = {'page_carte': page_carte, 'form': form}
                return render(request, 'blog/Cartes.html', context)

            date_t = request.POST['form-0-date']
            map_global(date_t)
            dynamic_superposition(date_t, parameters)
            page_carte = '/blog/map'
            context = {'page_carte': page_carte, 'form': form}

            time.sleep(5)
            # on renvoie une vue différente selon le choix d'affichage de l'utilisateur:

            if request.POST['form-0-choix_data'] == 'Cartes Séparées':
                return render(request, 'blog/maps/quadramap.html', context)
            else:
                return render(request, 'blog/maps/map_dynamic_superposition.html', context)

    else:

        form = FormulaireCarte()
        context = {'page_carte': page_carte, 'form': form}
        return render(request, 'blog/Cartes.html', context)


def mapview(request):
    return render(request, 'blog/maps/map.html')


# Quatres vues pour afficher simultanément sur une même page les différentes cartes (de manière non superposée).
def precipitation(request):
    return render(request, 'blog/maps/map_precipitation.html')


def pressure(request):
    return render(request, 'blog/maps/map_pressure.html')


def ndvi(request):
    return render(request, 'blog/maps/map_ndvi.html')


def temperature(request):
    return render(request, 'blog/maps/map_temperature.html')
