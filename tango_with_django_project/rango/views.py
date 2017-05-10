from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # construct a dictionary to pass to the template engine as its context.
    # note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunch, creamy, cookie, candy, cupcake!"}

    # return a rendered response to send to the client
    # we make use of the shortcut function to make our lives easier
    # note that the first parameter is the template we wish to use
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html')
