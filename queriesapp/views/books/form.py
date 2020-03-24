from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from queriesapp.models import Book
from ..connection import Connection
from queriesapp.models import Agent
from .detail import get_book



def get_books():
    if request.method == 'GET':
        all_books = Book.objects.all()
    return all_books



@login_required
def book_form(request):
    if request.method == 'GET':
        template = 'books/form.html'
        # context = {
        #     'all_agents': agents
        # }
        

        return render(request, template)

@login_required
def book_edit_form(request, book_id):

    if request.method == 'GET':
        book = get_book(book_id)
        
        template = 'books/form.html'
        context = {
            'book': book,
        }

        return render(request, template, context)