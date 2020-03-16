from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Query
from ..connection import Connection


def query_list(request):
    if request.method == 'GET':
        all_queries = Query.objects.all()

        # notes = request.GET.get('notes', None)   

        # if notes is not None:
        #     all_queries = all_queries.filter(notes__contains=notes)

        # agent_name = request.GET.get('agent_name', None)
        
        # if agent_name is not None:
        #     all_queries = all_queries.filter(query__contains=query)

        template = 'queries/list.html'
        context = {
            'all_queries': all_queries
        }   

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST
        #instantiate
        new_query = Query(
            notes = form_data['notes'],
            agent_id = form_data['agent_id'],
            sent = form_data['sent'],
            expiration = form_data['expiration'],
            book_id = form_data['book_id'],
            status_id = form_data['status_id'],
            user_id = request.user.id
        )
        # and then save to the db
        print(new_query.user.username)
        new_query.save()

        return redirect(reverse('queriesapp:queries'))



