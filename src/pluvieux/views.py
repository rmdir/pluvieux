from django.http import HttpResponse
import time
import sys
from django.shortcuts import render
from datetime import datetime
from .utils.map import map_global
from .utils.map import dynamic_superposition
from .forms import FormulaireCarte
from .models import Event

def cartes(request):
    page_carte = "/maps/empty"

    if request.method == 'POST':
        form = FormulaireCarte(request.POST)
        if form.is_valid():
            parameters = request.POST.getlist('form-0-choix_data')
            date_t = request.POST['form-0-date']
            #time.sleep(5)
            #XXX: not working
            if request.POST['form-0-choix_data'] == 'cartes Séparées':
                return render(request, 'quadramap.html', context)
            else:
                m = dynamic_superposition(date_t, parameters)
                return HttpResponse(m.get_root().render())
    form = FormulaireCarte()
    context = {'page_carte': page_carte, 'form': form}
    return render(request, 'cartes.html', context)
