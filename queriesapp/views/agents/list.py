from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Agent
from ..connection import Connection
from django.contrib.auth.decorators import login_required
from django.db.models import Q



def agent_list(request):
    if request.method == 'GET':
        current_user = request.user.id

        search_agent = request.GET.get('agent_search', '')
        print(search_agent, "0000000000")

        if search_agent:
            all_agents = Agent.objects.filter(Q(agent_name__icontains=search_agent))
        else:
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
        
        new_agent = Agent.objects.create(
            agent_name = form_data['agent_name'],
            company = form_data['company'],
            email = form_data['email'],
            user_id = request.user.id
        )
        

        return redirect(reverse('queriesapp:queries_form'))
