from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from .connection import get_data

data = get_data()
#print (data)

def home(request):

    #return render_to_response('index.html', {'dictionary': data}, context_instance=RequestContext(request))
    return render(request, 'index.html', {'data':data} )
