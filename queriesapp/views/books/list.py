from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Book
from ..connection import Connection



def book_list(request):
    if request.method == 'GET':
        all_agents = Book.objects.all()

        template = 'books/list.html'
        # context = {
        #     'all_books': all_books
        # }   

        return render(request, template)



    # elif request.method == 'POST':
    #     form_data = request.POST
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

        # new_agent = Agent.objects.create(
        #     agent_name = form_data['agent_name'],
        #     company = form_data['company'],
        #     email = form_data['email'],
        #     # user_id = request.user.id
        # )
        

        return redirect(reverse('queriesapp:queries'))
