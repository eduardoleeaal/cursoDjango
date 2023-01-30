from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def my_home(request):
    return render(request, 'recipes/home.html')


def my_contact(request):
    return HttpResponse('Contact')


def about_me(request):
    return HttpResponse('About Me')
