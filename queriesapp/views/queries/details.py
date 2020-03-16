from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from queriesapp.models import Query
from ..connection import Connection

def get_query(query_id):

    return Query.objects.get(pk=query_id)

# @login_required dd
def query_details(request, query_id):
    if request.method == 'GET':
        query = get_query(query_id)
        template_name = 'queries/detail.html'
        return render(request, template_name, {'query': query})

    elif request.method == 'POST':
        form_data = request.POST
    
    if (
        "actual_method" in form_data
        and form_data["actual_method"] == "DELETE"
        ):

        query = Query.objects.get(pk=query_id)
        query.delete()

        return redirect(reverse('queriesapp:queries'))

    