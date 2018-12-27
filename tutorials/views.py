from django.shortcuts import render
from .models import Tutorial


def tutorials(request):
    tutorials = Tutorial.objects.all()
    context = {
        'tutorials': tutorials
    }

    return render(request, 'tutorials/tutorials.html', context)


def tutorial(request):
    return render(request, 'tutorials/tutorial.html')


def search(request):
    return render(request, 'tutorials/search.html')
