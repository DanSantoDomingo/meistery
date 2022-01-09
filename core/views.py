from django.shortcuts import render, redirect

from core.forms import RequestForm 



def index(request):
 
    return redirect('core:home')



def home(request):
    context = {
        'form': RequestForm()
    }
    return render(request, 'core/index.html', context) 