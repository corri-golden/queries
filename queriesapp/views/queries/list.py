from django.shortcuts import render, render, reverse, redirect
from queriesapp.models import Query, Book
from ..connection import Connection



def query_list(request):
    if request.method == 'GET':
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
            'book': all_tacos
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

        return redirect(reverse('queriesapp:queries'))



