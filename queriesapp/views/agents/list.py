from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Agent
from ..connection import Connection



def agent_list(request):
    if request.method == 'GET':
        all_agents = Agent.objects.all()

        template = 'agents/list.html'
        context = {
            'all_agents': all_agents
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
            # user_id = request.user.id
        )
        

        return redirect(reverse('queriesapp:queries'))
