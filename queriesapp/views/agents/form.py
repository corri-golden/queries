import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from queriesapp.models import Agent
from ..connection import Connection
from queriesapp.models import Agent


def get_agents():
    # if request.method == 'GET':
    all_agents = Agent.objects.all()
    return all_agents



# @login_required
def agents_form(request):
    if request.method == 'GET':
        template = 'agents/form.html'
        # context = {
        #     'all_agents': agents
        # }

# @login_required
# def agent_edit_form(request, agent_id):

    # if request.method == 'GET':
    #     agent = get_agent(agent_id)

    #     template = 'agents/form.html'
    #     context = {
    #         'agent': agent,
    #     }

        return render(request, template)
        
