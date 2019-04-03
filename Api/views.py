from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def author(request):
    return HttpResponse('hello api')
