from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.view_habit, name='view_habit'),
    path('add/', views.add, name='add'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('check_off/<int:id>', views.check_off, name='check_off'),
    path('<int:id>', views.view_completed_dates, name='view_completed_dates'),
    path('<int:id>', views.view_inactivity_dates, name='view_inactivity_dates'),
]