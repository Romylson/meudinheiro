from django import forms

from .models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        # fields = ['nome','descricao','tipo']
        # fields = '__all__'
        exclude = ['usuario']
