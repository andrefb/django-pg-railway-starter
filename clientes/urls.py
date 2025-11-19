from django.urls import path
from .views import clientes_list, ClienteDetailView, ClienteEditView

app_name = 'clientes'

urlpatterns = [
    path('', clientes_list, name='list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='view'),
    path('<int:pk>/edit/', ClienteEditView.as_view(), name='edit'),
]
