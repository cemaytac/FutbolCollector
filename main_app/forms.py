from django.forms import ModelForm
from .models import Stats, Training


class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = ['date', 'goals', 'assists',
                  'clean_sheets', 'shots', 'appearances']
