from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
from models import *

def list(request,model,form):
	model_name = model.__name__.lower()
	empty_form = form()
	items = model.objects.all()
	template_name = '%s_list.html' % model_name
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': empty_form, 'action': reverse('%s_add' % model_name), 'button_label': 'Add',  }, 
	)

def add(request,model,form):
	model_name = model.__name__.lower()
	if request.method == 'POST':
		new_model = form(request.POST)
		if new_model.is_valid():
			new_model.save()
			return redirect(reverse(model_name))

	items = model.objects.all()
	template_name = '%s_list.html' % model_name
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': new_model, 'action': reverse("%s_add" % model_name), 'button_label': 'Add',  }, 
	)

def delete(request,model,model_id):
	model_name = model.__name__.lower()
	item = get_object_or_404(model, pk=model_id)
	item.delete()
	template_name = '%s_list.html' % model.__name__.lower()
	return redirect(reverse(model_name))

def edit(request,model, form, model_id):
	model_name = model.__name__.lower()
	item = get_object_or_404(model, pk=model_id)
	edit_form = form(request.POST or None, instance=item)
	if edit_form.is_valid():
		item = edit_form.save()
		item.save()
		return redirect(reverse(model_name))

	items = model.objects.all()
	template_name = '%s_list.html' % model_name
	return render(
		request,
		template_name, 
		{ 'items': items, 'form': edit_form, 'action': reverse("%s_edit" % model_name,  kwargs={ 'model_id': model_id }), 'button_label': 'Update'}, 
	)

def appointments_for_doctor(request, model_id, model):
	item = get_object_or_404(model, pk=model_id)
	items = item.appointment_set.all()
	template_name = 'appointment_list.html'
	return render(
		request,
		template_name, 
		{ 'items': items, 'title': item.name }, 
	)
