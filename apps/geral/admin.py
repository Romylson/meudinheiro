from django.contrib import admin
from .models import Categoria
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'usuario']
    search_fields = ['nome', 'usuario__username']
    list_filter = ['nome', 'usuario__username']


admin.site.register(Categoria,CategoriaAdmin)
