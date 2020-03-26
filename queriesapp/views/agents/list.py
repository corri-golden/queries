from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Agent
from ..connection import Connection
from django.contrib.auth.decorators import login_required



def agent_list(request):
    if request.method == 'GET':
        current_user = request.user.id

        all_agents = Agent.objects.filter(user_id=current_user).all()

    
        
        bookid = request.GET.get('bookid', None)   
        template = 'agents/list.html'
        context = {
            'all_agents': all_agents,
            'book_id': bookid
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

        new_agent = Agent.objects.create(
            agent_name = form_data['agent_name'],
            company = form_data['company'],
            email = form_data['email'],
            user_id = request.user.id
        )
        

        return redirect(reverse('queriesapp:queries_form'))
