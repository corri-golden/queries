from django.urls import include, path
from .views import *

app_name = "queriesapp"

urlpatterns = [
    path('', query_list, name='home'),
    path('queries/', query_list, name='queries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('queries/form', queries_form, name='queries_form'),
    path('queries/<int:query_id>/', query_details, name='query'),
]