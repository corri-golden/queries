import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from queriesapp.models import Query
from ..connection import Connection

# @login_required
def queries_form(request):
    if request.method == 'GET':
        template = 'queries/form.html'

        return render(request, template)