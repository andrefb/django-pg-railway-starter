from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informações adicionais', {'fields': ('nome', 'telefone', 'cpf')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações adicionais', {
            'classes': ('wide',),
            'fields': ('nome', 'telefone', 'cpf', 'username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'nome', 'telefone', 'cpf', 'is_staff')
