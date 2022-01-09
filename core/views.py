from django.shortcuts import render

from core.forms import RequestForm 



def index(request):
    context = {
        'form': RequestForm()
    }
    return render(request, 'core/index.html', context) 



