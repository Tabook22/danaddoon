from django.shortcuts import render
from .models import Tutorial 

def tutorials(request):
    tutorials=Tutorial.objects.all()
    
    return render(request, 'tutorials/tutorials.html')

def tutorial(request):
    return render(request, 'tutorials/tutorial.html')

def search(request):
    return render(request, 'tutorials/search.html')