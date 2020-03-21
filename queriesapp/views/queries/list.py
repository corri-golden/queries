from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Query, Book
from ..connection import Connection


#This gets all the queries that the logged in user has added.
# @login_required
def query_list(request):
    if request.method == 'GET':
        
        current_user = request.user
        user_queries = Query.objects.filter(user=current_user)
        
        all_queries = Query.objects.all()
        all_tacos=Book.objects.all()
        bookid = request.GET.get('bookid', None)   
        
        if bookid is not None:
            all_queries = all_queries.filter(book_id=bookid)
        
            all_tacos=Book.objects.filter(id=bookid)[0]
        # agent_name = request.GET.get('agent_name', None)
        
        # if agent_name is not None:
        #     all_queries = all_queries.filter(query__contains=query)

        
        # taco is the variable that holds the book we got back from the filter
        template = 'queries/list.html'
        context = {
            'all_queries': all_queries,
            'book': all_tacos,
            # 'user_queries': user_queries
        }   
        # book is a variable that holds the taco variable.  we are creating the book variable. then pass to context to the queries list template.  context is passed to the template. now have access book.  book.name
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

    # attempt at carrying the book id and using it
    # elif request.method == 'POST':
    #     form_data = request.POST

    #     bookid = request.GET.get('bookid', NONE)
    #     new_query = Query()

    #     if bookid is not None:
            
    #         new_query = Query(
    #         notes = form_data['notes'],
    #         agent_id = form_data['agent_id'],
    #         sent = form_data['sent'],
    #         expiration = form_data['expiration'],
    #         book_id = bookid,
    #         status_id = form_data['status_id'],
    #     )

    #     print(new_query.user.username)
    #     new_query.save()
    #     return redirect(reverse('/queries?bookid={{bookid}}'))
        # end attempt

         





        return redirect(reverse('queriesapp:queries'))
    



