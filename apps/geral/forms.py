from django import forms

from .models import Categoria

class CategoriaForm(forms.ModelForm):
# nome = forms.CharField(label='Nome', widget=forms.TextInput(attrs={'class':'forms-control'}))

    class Meta:
        model = Categoria
        # fields = ['nome','descricao','tipo']
        # fields = '__all__'
        exclude = ['usuario']
