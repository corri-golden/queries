from django.urls import include, path
from .views import *

app_name = "queriesapp"

urlpatterns = [
    path('', book_list, name='home'),
    path('queries/', query_list, name='queries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('queries/form', queries_form, name='queries_form'),
    path('queries/<int:query_id>/', query_details, name='query'),
    path('agents/form', agents_form, name='agents_form'),
    path('agents/', agent_list, name='agents'),
    path('books/form', book_form, name='book_form'),
]