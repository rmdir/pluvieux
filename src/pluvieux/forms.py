from django import forms
from .models import Event
from django.forms import widgets
from django.forms import formset_factory


class SelectDateForm(forms.Form):

    region = forms.ChoiceField( choices=[
        ('option1', 'Europe'),
        ('option2', 'Amérique du Nord'),
        ('option3', 'Amérique du Sud'),
        ('option4', 'Afrique'),
        ('option5', 'Asie'),
        ('option6', 'Océanie'),
        ('option7', 'Monde') ], 
        widget=forms.Select, label='Région'
    )
    date = forms.DateField(
        label="Date",
        widget=widgets.DateInput(attrs={'type': 'date'}),
        input_formats=["%Y-%m-%d"]
    )
    choix_data = forms.MultipleChoiceField( choices=[
        ('cartes Séparées', 'Cartes Séparées'),
        ('Indice de végétation', 'Indice de végétation'),
        ('Température', 'Température'),
        ('Pression', 'Pression'),
        ('Précipitations', 'Précipitations') ], 
    widget=forms.CheckboxSelectMultiple, label="Choix des données à afficher")
    def clean_date(self):
        d = self.cleaned_data["date"]
        if not d:
          raise ValidationError("You have forgotten about Fred!")
        return d



FormulaireCarte = formset_factory(SelectDateForm, extra=1)
