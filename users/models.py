from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):    
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, blank=True)
    nome = models.CharField(max_length=150, blank=True)  # Nome completo

    # Remova first_name/last_name dos forms se quiser só nome
