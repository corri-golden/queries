from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from queriesapp.models import Status
from ..connection import Connection



def get_status(status_id):

    return Status.objects.get(pk=status_id)