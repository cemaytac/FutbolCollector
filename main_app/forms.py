from django.forms import ModelForm
from .models import Stats


class StatsForm(ModelForm):
    class Meta:
        model = Stats
        fields = ['appearances', 'goals', 'assists', 'clean_sheets', 'shots']
