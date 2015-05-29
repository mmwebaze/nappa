#!/usr/bin/env python3
from django.shortcuts import render
from .forms import FacilityForm, ClientForm, ServiceForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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