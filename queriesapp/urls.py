from django.urls import path
from .views import *

app_name = "queriesapp"

urlpatterns = [
    path('', query_list, name='home'),
    path('queries/', query_list, name='queries'),
    path('queries/form', queries_form, name='queries_form'),
    path('queries/<int:query_id>/', query_details, name='query'),
]