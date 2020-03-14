from django.shortcuts import render, render, reverse
from queriesapp.models import Query
from ..connection import Connection


def query_list(request):
    if request.method == 'GET':
        all_queries = Query.objects.all()

        # notes = request.GET.get('notes', None)   

        # if notes is not None:
        #     all_queries = all_queries.filter(notes__contains=notes)

        template = 'queries/list.html'
        context = {
            'all_queries': all_queries
        }   

        return render(request, template, context)