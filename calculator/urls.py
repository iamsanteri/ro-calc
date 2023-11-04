## Render the views for the calculator app
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]