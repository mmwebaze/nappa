#!/usr/bin/env python3
from django.shortcuts import render
from .forms import FacilityForm, ClientForm, ServiceForm, FamilyPlanningCardForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from nappaadmin.models import Client
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

#from .forms import ClientForm
#from .forms import ServiceForm

@login_required
def facility(request):
	form = FacilityForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		
	context = {"form" : form}
	template = "facility.html"
	return render(request, template, context)

@login_required	
def client(request):
	form = ClientForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		
	context = {"form" : form}
	template = "client.html"
	return render(request, template, context)

@login_required
def service(request):
	form = ServiceForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
		
	context = {"form" : form}
	template = "service.html"
	return render(request, template, context)

@login_required
def clientlist(request):
	allclients = Client.objects.all()
	client_list = {"clients" : allclients}	
	template = "client_list.html"
	return render_to_response(template, client_list)
	
@login_required
def familyplanningcard(request):
	form = FamilyPlanningCardForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	
	context = {"form" : form}
	template = "fpcard.html"
	return render(request, template, context)

def search(request):
	template = "fpcard.html"
	if request.method == 'POST':
		searchform = SearchForm(request.POST or None)
		if form.is_valid():
			
			return HttpResponseRedirect('/fpcard/')
		else:
			searchform = SearchForm()
		return render(request, template, {'searhform' : searchform})