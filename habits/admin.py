from django.contrib import admin
from .models import Habit, CompletedHabit, Inactivity

# Register your models here.
admin.site.register(Habit)
admin.site.register(CompletedHabit)
admin.site.register(Inactivity)