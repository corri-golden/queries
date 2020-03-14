from django.urls import path
from .views import *

app_name = "queriesapp"

urlpatterns = [
    path('', query_list, name='home'),
    path('queries/', query_list, name='queries'),
]