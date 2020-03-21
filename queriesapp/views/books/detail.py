from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from queriesapp.models import Query, Agent, Book
from ..connection import Connection





def get_book(book_id):
    return Book.objects.get(pk=book_id)


# @login_required dd
def book_details(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)
        template = 'books/detail.html'
        return render(request, template, {'book': book})

    # elif request.method == 'POST':
    #     form_data = request.POST

    # if (
    #         "actual_method" in form_data
    #         and form_data["actual_method"] == "PUT"
    #     ):

    #     # # retrieve it first:
    #     book_to_update = Book.objects.get(pk=book_id)

    #     # # Reassign a property's value
    #     book_to_update.book_name = form_data['book_name']
    #     book_to_update.num_of_pages = form_data['num_of_pages']
            
    #     # # Save the change to the db
    #     book_to_update.save()

        # return redirect(reverse('queriesapp:queries'))

        