from django.db import models
from django.conf import settings

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    rg_num = models.CharField(max_length=20, blank=True)
    rg_data = models.DateField(null=True, blank=True)
    rg_orgao = models.CharField(max_length=50, blank=True)
    logradouro = models.CharField(max_length=255, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    uf = models.CharField(max_length=2, blank=True)
    cep = models.CharField(max_length=10, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    id_usuario_update = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='clientes_atualizados'
    )
    id_corretor = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nome
