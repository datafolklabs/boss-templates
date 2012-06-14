# Create your views here.

from django.shortcuts import render, redirect

def index(request):
    data = {}
    return render(request, 'examples/index.html', data)

def create(request):
    data = {}
    return render(request, 'examples/create.html', data)

def update(request, examples_id):
    data = {}
    return render(request, 'examples/update.html', data)

def delete(request, examples_id):
    data = {}
    return render(request, 'examples/delete.html', data)

def details(request, examples_id):
    data = {}
    return render(request, 'examples/details.html', data)

def manage(request):
    data = {}
    return render(request, 'examples/manage.html', data)



