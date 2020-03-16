import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from queriesapp.models import Query
from ..connection import Connection
from queriesapp.models import Agent


def get_agents():
    # if request.method == 'GET':
    all_agents = Agent.objects.all()
    return all_agents



# @login_required
def queries_form(request):
    if request.method == 'GET':
        agents = get_agents()
        template = 'queries/form.html'
        context = {
            'all_agents': agents
        }
        

        return render(request, template, context)