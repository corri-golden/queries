from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from queriesapp.models import Agent
from ..connection import Connection

def get_agent(agent_id):

    return Agent.objects.get(pk=agent_id)

# @login_required dd
def agent_details(request, agent_id):
    if request.method == 'GET':
        agent = get_agent(agent_id)
        template_name = 'agents/detail.html'
        return render(request, template_name, {'agent': agent})

    elif request.method == 'POST':
        form_data = request.POST

    if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

        # # retrieve it first:
        agent_to_update = Agent.objects.get(pk=agent_id)

        # # Reassign a property's value
        agent_to_update.agent_name = form_data['agent_name']
        agent_to_update.company = form_data['company']
        agent_to_update.email = form_data['email']
            
        # # Save the change to the db
        agent_to_update.save()

        return redirect(reverse('queriesapp:agents'))

    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
        ):

    

        agent = Agent.objects.get(pk=agent_id)
        agent.delete()

        return redirect(reverse('queriesapp:agents'))