from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from queriesapp.models import Query, Agent
from ..connection import Connection


def get_query(query_id):

    return Query.objects.get(pk=query_id)

def get_agent(agent_id):

    return Agent.objects.get(pk=agent_id)

# @login_required dd
def query_details(request, query_id):
    if request.method == 'GET':
        query = get_query(query_id)
        template_name = 'queries/detail.html'
        return render(request, template_name, {'query': query})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
    if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
        
        # # retrieve it first:
        query_to_update = Query.objects.get(pk=query_id)
        

        # # Reassign a property's value
        query_to_update.sent = form_data['sent']
        query_to_update.expiration = form_data['expiration']
        query_to_update.notes = form_data['notes']
        query_to_update.agent_id = form_data['agent_id']
         # # Save the change to the db
        query_to_update.save()

        # # retrieve it first:
        agent_to_update = Agent.objects.get(pk=query_to_update.agent_id)
        agent_to_update.email = form_data['email']
        agent_to_update.company = form_data['company']
        
        agent_to_update.save()

        return redirect(reverse('queriesapp:queries'))
    
    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
        ):

        query = Query.objects.get(pk=query_id)
        query.delete()

        return redirect(reverse('queriesapp:queries'))

    