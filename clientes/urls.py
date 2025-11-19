from django.urls import path
from .views import ClienteListView, ClienteDetailView, ClienteEditView

app_name = 'clientes'

urlpatterns = [
    path('', ClienteListView.as_view(), name='list'),
    path('<int:pk>/', ClienteDetailView.as_view(), name='view'),
    path('<int:pk>/edit/', ClienteEditView.as_view(), name='edit'),
]
