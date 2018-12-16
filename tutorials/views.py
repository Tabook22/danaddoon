from django.shortcuts import render

def tutorials(request):
    return render(request, 'tutorials/tutorials.html')

def tutorial(request):
    return render(request, 'tutorials/tutorial.html')

def search(request):
    return render(request, 'tutorials/search.html')