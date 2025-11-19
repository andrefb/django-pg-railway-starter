from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        exclude = ['updated_at', 'id_usuario_update', 'id_corretor']
