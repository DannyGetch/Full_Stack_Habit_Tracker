import datetime
from time import strptime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Habit, CompletedHabit, Inactivity
from .forms import HabitForm
from django.db import models

from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'habits/index.html', {
        'habits': Habit.objects.all(),
        'completed_dates': CompletedHabit.objects.all(),
        'inactivity_dates': Inactivity.objects.all()
    })

def view_habit(request, id):
    habit = Habit.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data['name']
            new_periodicity= form.cleaned_data['periodicity']
            new_duration = form.cleaned_data['duration']
          
            new_habit = Habit(
                name = new_name,
                periodicity = new_periodicity,
                duration = new_duration
            )

            if(new_habit.periodicity == "Daily"):
                new_habit.streak_type = "day(s)"
            elif(new_habit.periodicity == "Weekly"):
                new_habit.streak_type = "week(s)"
            elif(new_habit.periodicity == "Monthly"):
                new_habit.streak_type = "month(s)"
            elif(new_habit.periodicity == "Yearly"):
                new_habit.streak_type = "year(s)"

            new_habit.save()
            return render(request, 'habits/add.html', {
                'form': HabitForm(),
                'success': True
            })
    else:
        form = HabitForm()
    return render(request, 'habits/add.html', {
        'form': HabitForm()
    })

def edit(request, id):
    if request.method == 'POST':
        habit = Habit.objects.get(pk=id)
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return render(request, 'habits/edit.html', {
                'form': form,
                'success': True
            })
    else:
        habit = Habit.objects.get(pk=id)
        form = HabitForm(instance=habit)
    return render(request, 'habits/edit.html', {
        'form': form
    })

def delete(request, id):
    if request.method == 'POST':
        habit = Habit.objects.get(pk=id)
        habit.delete()
        messages.success(request, "Habit deleted successfully!")
    return HttpResponseRedirect(reverse('index'))

def complete_habit(habit):
    completed_habit = CompletedHabit(name=habit)
    completed_habit.save()             
    habit.last_completed_date = completed_habit.completed_date
    habit.streak += 1
    habit.save()

def reset_streak(habit):
    completed_habit = CompletedHabit(name=habit)
    completed_habit.save()     
    inactive = Inactivity(name=habit, first_inactive_date=habit.last_completed_date)
    inactive.save()        
    habit.last_completed_date = completed_habit.completed_date
    habit.streak = 1
    habit.save()

def check_off(request, id):
    if request.method == 'POST':
        habit = Habit.objects.get(pk=id)
        current_time = datetime.datetime.now()
        
       
        if(habit.periodicity == "Daily"):
            if(habit.last_completed_date == None):   
                complete_habit(habit)
                messages.success(request, "Great! You're on the first day of your streak.")
            else:
                d1 = datetime.datetime.strptime(str(habit.last_completed_date), "%Y-%m-%d %H:%M:%S.%f").date()
                d2 = datetime.datetime.strptime(str(current_time), "%Y-%m-%d %H:%M:%S.%f").date()
                diff=(d2-d1).days

                if(diff == 0):
                    messages.error(request, "You have already completed this habit today. Try tomorrow!")
                elif(diff == 1):
                    complete_habit(habit)
                    messages.success(request, f"You're doing great! You have a new streak of {habit.streak} days. Keep it up!")
                else:
                    messages.error(request, f"You've broken your streak. You've been inactice for {diff} days. We're starting over!")
                    reset_streak(habit)

        elif(habit.periodicity == "Weekly"):
            if(habit.last_completed_date == None):   
                complete_habit(habit)
                messages.success(request, "Great! You're on the first week of your streak.")
            else:
                d1 = datetime.datetime.strptime(str(habit.last_completed_date), "%Y-%m-%d %H:%M:%S.%f").date()
                d2 = datetime.datetime.strptime(str(current_time), "%Y-%m-%d %H:%M:%S.%f").date()
                monday1 = (d1 - datetime.timedelta(days=d1.weekday()))
                monday2 = (d2 - datetime.timedelta(days=d2.weekday()))
                diff = (monday2 - monday1).days / 7

                if(diff == 0):
                    messages.error(request, "You have already completed this habit this week. Try next week!")
                elif(diff == 1):
                    complete_habit(habit)
                    messages.success(request, f"You're doing great! You have a new streak of {habit.streak} weeks. Keep it up!")
                else:
                    messages.error(request, f"You've broken your streak. You've been inactice for {diff} weeks. We're starting over!")
                    reset_streak(habit)
        
        elif(habit.periodicity == "Monthly"):
            if(habit.last_completed_date == None):   
                complete_habit(habit)
                messages.success(request, "Great! You're on the first month of your streak.")
            else:
                d1 = datetime.datetime.strptime(str(habit.last_completed_date), "%Y-%m-%d %H:%M:%S.%f").date()
                d2 = datetime.datetime.strptime(str(current_time), "%Y-%m-%d %H:%M:%S.%f").date()
                month1 = d1.month
                month2 = d2.month
                diff = (month2 - month1)

                if(diff < 0):
                    diff += 12

                if(diff == 0):
                    messages.error(request, "You have already completed this habit this month. Try next month!")
                elif(diff == 1):
                    complete_habit(habit)
                    messages.success(request, f"You're doing great! You have a new streak of {habit.streak} months. Keep it up!")
                else:
                    messages.error(request, f"You've broken your streak. You've been inactice for {diff} months. We're starting over!")
                    reset_streak(habit)

        elif(habit.periodicity == "Yearly"):
            if(habit.last_completed_date == None):   
                complete_habit(habit)
                messages.success(request, "Great! You're on the first year of your streak.")
            else:
                d1 = datetime.datetime.strptime(str(habit.last_completed_date), "%Y-%m-%d %H:%M:%S.%f").date()
                d2 = datetime.datetime.strptime(str(current_time), "%Y-%m-%d %H:%M:%S.%f").date()
                year1 = d1.year
                year2 = d2.year
                diff = year2 - year1

                if(diff == 0):
                    messages.error(request, "You have already completed this habit this year. Try next year!")
                elif(diff == 1):
                    complete_habit(habit)
                    messages.success(request, f"You're doing great! You have a new streak of {habit.streak} years. Keep it up!")
                else:
                    messages.error(request, f"You've broken your streak. You've been inactice for {diff} years. We're starting over!")
                    reset_streak(habit)
                
    return HttpResponseRedirect(reverse('index'))

def view_completed_dates(request, id):
    completed_date = CompletedHabit.objects.get(fk=id)
    return HttpResponseRedirect(reverse('index'))

def view_inactivity_dates(request, id):
    completed_date = Inactivity.objects.get(fk=id)
    return HttpResponseRedirect(reverse('index'))