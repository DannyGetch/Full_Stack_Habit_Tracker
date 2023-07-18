from django.test import TestCase
from habits.models import Habit
from . import views
from freezegun import freeze_time

from django.http import HttpRequest

import pytest


@pytest.mark.django_db  # give test access to database
def test_habit_create():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    assert daily_habit.name == "Laugh"
    assert yearly_habit.name == "Trip to Kenya"


@pytest.mark.django_db  # give test access to database
def test_habit_delete():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")

    daily_habit.delete()
    assert daily_habit.DoesNotExist

    yearly_habit.delete()
    assert yearly_habit.DoesNotExist


@freeze_time("01/02/2023 12:42")
@pytest.mark.django_db  # give test access to database
def test_habit_checkoff():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    r = HttpRequest
    r.method = 'GET'
    views.check_off(r, daily_habit.id)
    views.check_off(r, yearly_habit.id)


@freeze_time("01/03/2023 12:42")
@pytest.mark.django_db  # give test access to database
def test_habit_checkoff_second():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    r = HttpRequest
    r.method = 'GET'
    views.check_off(r, daily_habit.id)
    views.check_off(r, yearly_habit.id)


@freeze_time("01/04/2023 12:42")
@pytest.mark.django_db  # give test access to database
def test_habit_checkoff_third():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    r = HttpRequest
    r.method = 'GET'
    views.check_off(r, daily_habit.id)
    views.check_off(r, yearly_habit.id)


@freeze_time("01/05/2023 12:42")
@pytest.mark.django_db  # give test access to database
def test_habit_checkoff_fourth():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    r = HttpRequest
    r.method = 'GET'
    views.check_off(r, daily_habit.id)
    views.check_off(r, yearly_habit.id)


@freeze_time("01/06/2023 12:42")
@pytest.mark.django_db  # give test access to database
def test_habit_checkoff_fifth():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    r = HttpRequest
    r.method = 'GET'
    views.check_off(r, daily_habit.id)
    views.check_off(r, yearly_habit.id)


@freeze_time("01/07/2023 12:42")
@pytest.mark.django_db  # give test access to database
def test_habit_checkoff_sixth():
    daily_habit = Habit.objects.create(
        name="Laugh", periodicity="Daily", duration="Always")
    yearly_habit = Habit.objects.create(
        name="Trip to Kenya", periodicity="Yearly", duration="10 years")
    r = HttpRequest
    r.method = 'GET'
    views.check_off(r, daily_habit.id)
    views.check_off(r, yearly_habit.id)
