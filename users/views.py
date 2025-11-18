from django.shortcuts import render

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CustomUser

@login_required
def account_profile(request):
    
    return render(request, 'account/profile.html')
