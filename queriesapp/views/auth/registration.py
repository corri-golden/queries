from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register_user(request):
    """Handles creation of a new user for auth
        Args:
        request = full http object
    """
    if request.method == "GET":
        template_name = 'registration/register.html'
        return render(request, template_name, {})

    # For handling when user submits the form data
    elif request.method == "POST":
        form_data = request.POST

        # First create a new user using django's built in craziness. create_user is a method in django.
        new_user = User.objects.create_user(
            # username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            username=request.POST['username'],
            # first_name=request.POST['first_name'],
            # last_name=request.POST['last_name']
        )

        authenticated_user = authenticate(
            email=form_data['email'],
            username=form_data['username'], 
            password=form_data['password']
        )

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return redirect(reverse('queriesapp:accounts'))

        else:
            # Bad login details were provided. We need to let them know they need to fix this.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")   

        

        # Second, make a librarian after the user has been created
        # librarian = Librarian.objects.create(
        #     user=new_user,
        #     # If you have other form data to save on the new librarian, that isn't a property of the User model...
        #     fave_color=request.POST['fave_color']
        # )

        # login(request, new_user)

        # Redirect the browser to wherever you want to go after registering
        # return redirect(reverse('queriesapp:accounts'))

    # handles a request to load the empty form for the useer to fill out
    # else:
    #     template = 'registration/register.html'

    # return render(request, template, {})