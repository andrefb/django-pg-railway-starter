# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import HomeView, AboutView, contact_view, ServicesView, FaqView, subscribe_view  # adjust the import based on your app structure

urlpatterns = [
    
    
    # Static pages
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path("contact/", contact_view, name="contact"),
    path('services/', ServicesView.as_view(), name='services'),
    path('faq/', FaqView.as_view(), name='faq'),
    path('subscribe/', subscribe_view, name='subscribe'),
]
