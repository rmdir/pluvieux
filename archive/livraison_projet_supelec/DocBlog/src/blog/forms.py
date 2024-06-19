from django import forms
from .models import Event
from django.forms import widgets
from django.forms import formset_factory


class SelectDateForm(forms.Form):

    #choixrégion = forms.ChoiceField(choices=[('option1', 'Europe'), (
     #   'option2', 'Amérique du Nord'), ('option3', 'Amérique du Sud'), ('option4', 'Afrique'), ('option5', 'Asie'), ('option6', 'Océanie'), ('option7', 'Monde')], widget=forms.Select, label='Région')

    date = forms.DateField(
        label="Date",
        widget=widgets.DateInput(attrs={'type': 'date'}),
        input_formats=["%Y-%m-%d"])

    choix_data = forms.MultipleChoiceField(choices=[('Cartes Séparées', 'Cartes Séparées'),
                                                           ('Indice de végétation',
                                                            'Indice de végétation'),
                                                           ('Température',
                                                            'Température'),
                                                           ('Pression',
                                                            'Pression'),
                                                           ('Précipitations',
                                                            'Précipitations')
                                                           ], widget=forms.CheckboxSelectMultiple, label="Choix des données à afficher")
    # à voir si on remet ce choix pour afficher seulement une donnée mais cela ne semble pas cohérent
    # choixdata = forms.ChoiceField(choices=[('Precipitation', 'Precipitation'), (
    # 'Temperature', 'Temperature'), ('Pressure', 'Pressure'), ('NDVI', 'NDVI')], widget=forms.Select, label='Choix des données')


FormulaireCarte = formset_factory(SelectDateForm, extra=1)
