from django.urls import path
from . import views
app_name = 'movimentacoes'

urlpatterns =[
    path('nova-movimentacao/', views.nova_movimentacao, name='nova_movimentacao'),
    path('minhas-movimentacoes/', views.lista_movimentacoes, name='lista_movimentacoes'),
]
