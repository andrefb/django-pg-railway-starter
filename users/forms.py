from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    nome = forms.CharField(label="Nome completo", max_length=150)
    telefone = forms.CharField(label="Telefone", max_length=20, required=False)
    cpf = forms.CharField(label="CPF", max_length=14, required=False)

    def save(self, request):
        user = super().save(request)
        user.nome = self.cleaned_data.get('nome')
        user.telefone = self.cleaned_data.get('telefone')
        user.cpf = self.cleaned_data.get('cpf')
        user.save()
        return user
