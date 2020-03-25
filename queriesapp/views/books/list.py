from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Book
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def book_list(request):
    if request.method == 'GET':
        current_user = request.user.id
        # user_queries = Query.objects.filter(user_id=current_user)
        
        all_books = Book.objects.filter(user_id=current_user).all()

        # all_books = Book.objects.all()

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }   

        return render(request, template, context)



    elif request.method == 'POST':
        form_data = request.POST
        #instantiate
        # new_agent = Agent(
        #     agent_name = form_data['agent_name'],
        #     company = form_data['company'],
        #     email = form_data['email'],
        #     user_id = request.user.id
        # )
        # # and then save to the db
        # print(new_agent.user.username)
        # new_agent.save()

        new_book = Book.objects.create(
            book_name = form_data['book_name'],
            num_of_pages = form_data['num_of_pages'],
            user_id = request.user.id
        )
        

        return redirect(reverse('queriesapp:books'))
