from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        PERIODICITY_CHOICES = [
            ('daily', 'Daily'),
            ('weekly', 'Weekly'),
            ('monthly', 'Monthly'),
        ]
        model = Habit
        fields = ['name', 'periodicity', 'duration']
        labels = {
            'name': 'Habit Name',
            'periodicity': 'Periodicity',
            'duration': 'Duration'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'periodicity': forms.TextInput(attrs={'class': 'form-control'}),
            #'periodicity': forms.ChoiceField(choices=PERIODICITY_CHOICES, attrs={'class': 'form-control'}),
            'duration': forms.TextInput(attrs={'class': 'form-control'})
        }