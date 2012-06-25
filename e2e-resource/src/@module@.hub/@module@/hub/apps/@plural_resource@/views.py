# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib import messages
from @module@.hub import db, forms

def list(request):
    data = {}
    data['@plural_resource@'] = db.@resource.capitalize@.objects.all()
    return render(request, '@plural_resource@/list.html', data)

def details(request, @resource@_id):
    data = {}
    data['@resource@'] = get_object_or_404(db.@resource.capitalize@, id=@resource@_id)
    return render(request, '@plural_resource@/details.html', data)

def create(request):
    data = {}
    if request.method == 'POST':
        form = forms.@resource.capitalize@Form(request.POST)
        if form.is_valid():
            @resource@ = form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 '%s created successfully' % @resource@.label)
            return redirect(reverse('manage_@plural_resource@'))
    else:
        form = forms.@resource.capitalize@Form(initial=dict(created_by=request.user))
    
    data['form'] = form
    return render(request, '@plural_resource@/create.html', data)

def update(request, @resource@_id):
    data = {}
    @resource@ = get_object_or_404(db.@resource.capitalize@, id=@resource@_id)
    
    if request.method == 'POST':
        form = forms.@resource.capitalize@Form(request.POST, instance=@resource@)
        if form.is_valid():
            @resource@ = form.save()
            messages.add_message(request, messages.SUCCESS, 
                                 '%s updated successfully' % @resource@.label)
            return redirect(reverse('update_@resource@',
                                    kwargs={'@resource@_id': @resource@.id}))                                
    else:
        form = forms.@resource.capitalize@Form(instance=@resource@)

    data['form'] = form
    data['@resource@'] = @resource@
    return render(request, '@plural_resource@/update.html', data)
    
def delete(request, @resource@_id):
    data = {}
    @resource@ = get_object_or_404(db.@resource.capitalize@, id=@resource@_id)
    @resource@.delete()
    messages.add_message(request, messages.WARNING, 
                                 '%s has been deleted.' % @resource@.label)
    return redirect(reverse('manage_@plural_resource@'))

def manage(request):
    data = {}
    data['@plural_resource@'] = db.@resource.capitalize@.objects.all()
    return render(request, '@plural_resource@/manage.html', data)
