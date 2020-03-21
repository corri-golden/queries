import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from queriesapp.models import Query, Book
from ..connection import Connection
from queriesapp.models import Agent
from .details import get_query


def get_query(query_id):

    return Query.objects.get(pk=query_id)

def get_agents():
    # if request.method == 'GET':
    all_agents = Agent.objects.all()
    return all_agents

def get_books():
    all_books = Book.objects.all()
    return all_books



# @login_required
def queries_form(request):
    if request.method == 'GET':
        agents = get_agents()
        books = get_books()
        template = 'queries/form.html'
        context = {
            'all_agents': agents,
            'all_books': books
        }

    return render(request, template, context)

# @login_required
def queries_edit_form(request, query_id):

    if request.method == 'GET':
        query = get_query(query_id)
        
        agents = get_agents()
        template = 'queries/form.html'
        context = {
            'query': query,
            'all_agents': agents
        }

        return render(request, template, context)
        

    