from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Your home app:
    path('', include('home.urls')),
    # allauth URLs for account management (login, signup, etc.)

    # ... your other URL patterns ...
    path('account/', include('users.urls')),
    path('accounts/', include('allauth.urls')),
]


