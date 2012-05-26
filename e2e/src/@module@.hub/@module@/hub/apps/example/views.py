# Create your views here.

from django.shortcuts import render, redirect

def index(request):
    data = {}
    return render(request, 'example/index.html', data)
