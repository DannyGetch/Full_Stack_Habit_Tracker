from django import forms
from .models import Habit

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'periodicity', 'duration']
        labels = {
            'name': 'Habit Name',
            'periodicity': 'Periodicity',
            'duration': 'Duration'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            #'periodicity': forms.TextInput(attrs={'class': 'form-control'}),
            #'periodicity': forms.ChoiceField(choices=PERIODICITY_CHOICES, attrs={'class': 'form-control'}),
            'periodicity': forms.RadioSelect(),
            'duration': forms.TextInput(attrs={'class': 'form-control'})
        }