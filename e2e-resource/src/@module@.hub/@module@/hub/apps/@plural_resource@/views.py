# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from kserver.hub import db, forms

def list(request):
    data = {}
    return render(request, 'environments/list.html', data)

def details(request, env_id):
    data = {}
    data['environment'] = get_object_or_404(db.@resource_class_prefix@, id=env_id)
    return render(request, 'environments/details.html', data)

def create(request):
    data = {}
    if request.method == 'POST':
        form = forms.@resource_class_prefix@Form(request.POST)
        if form.is_valid():
            env = form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 '%s created successfully' % env.label)
            return redirect(reverse('manage_environments'))
    else:
        form = forms.@resource_class_prefix@Form(initial=dict(created_by=request.user))
    
    data['form'] = form
    return render(request, 'environments/create.html', data)

def update(request, env_id):
    data = {}
    env = get_object_or_404(db.@resource_class_prefix@, id=env_id)
    
    if request.method == 'POST':
        form = forms.@resource_class_prefix@Form(request.POST, instance=env)
        if form.is_valid():
            env = form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 '%s updated successfully' % env.label)
            return redirect(reverse('update_environment',
                                    kwargs={'env_id': env.id}))                                
    else:
        form = forms.@resource_class_prefix@Form(instance=env)

    data['form'] = form
    data['environment'] = env
    return render(request, 'environments/update.html', data)
    
def delete(request, env_id):
    data = {}
    env = get_object_or_404(db.@resource_class_prefix@, id=env_id)
    env.delete()
    messages.add_message(request, messages.WARNING, 
                                 '%s has been deleted.' % env.label)
    return redirect(reverse('manage_environments'))

def manage(request):
    data = {}
    data['environments'] = db.@resource_class_prefix@.objects.all()
    return render(request, 'environments/manage.html', data)
