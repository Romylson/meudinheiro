from django.urls import path

app_name = 'geral'

from geral import views

urlpatterns = [
    path('', views.principal, name='principal'),
]