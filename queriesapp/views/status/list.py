from django.shortcuts import render
from queriesapp.models import Status
from ..connection import Connection


def status_list(request):
    if request.method == 'GET':
        all_statuses = Status.objects.all()

        template = 'status/list.html'
        context = {
            'all_statuses': all_statuses
        }   
        print("status: ", all_statuses)
        return render(request, template, context)
        