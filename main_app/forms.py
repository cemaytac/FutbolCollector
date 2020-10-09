from django import forms
from django.forms import ModelForm
from .models import Stats, Training

CHOICES = [('Yes'), ('No')]
choice_field = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
choice_field.choices
choice_field.widget.choices


class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = ['date', 'goals', 'assists',
                  'clean_sheets', 'shots', 'appearances']
