from django.db import models
from django import forms


PERIODICITY_CHOICES = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly')
    ]

class Habit(models.Model):
    
    name = models.CharField(max_length=50)
    periodicity = models.CharField(
        max_length=10,
        choices=PERIODICITY_CHOICES,
        default='Daily',
        )
    duration = models.CharField(max_length=20)
    streak = models.IntegerField(default=0)
    streak_type = models.CharField(max_length=10, blank = True)
    created_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank=True)
    last_completed_date = models.DateTimeField(auto_now_add = False, auto_now=False,  blank=True, null=True)

    def __str__(self):
        return f'Habit: {self.name} {self.periodicity}'
    
class CompletedHabit(models.Model):
    name = models.ForeignKey(Habit, on_delete=models.CASCADE)
    completed_date =  models.DateTimeField(auto_now_add = True, auto_now = False, blank=True)

    def __str__(self):
        return f'{self.completed_date}'

class Inactivity(models.Model):
    name = models.ForeignKey(Habit, on_delete=models.CASCADE)
    first_inactive_date = models.DateTimeField(auto_now_add = False, auto_now = False, blank=True)
    last_inactive_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank=True)