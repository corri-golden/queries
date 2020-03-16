from django.urls import reverse
from django.shortcuts import redirect
# from django.contrib.auth import logout_user

def logout_user(request):
    logout(request)
    return redirect(reverse('queriesapp:home'))