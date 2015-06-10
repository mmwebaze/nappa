#!/usr/bin/env python3
from django.shortcuts import render, get_object_or_404
from .forms import FacilityForm, ClientForm, ServiceForm, ClientVisitForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from nappaadmin.models import Client, ClientVisit
from django.shortcuts import render_to_response
from datetime import datetime
from django.utils import formats

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
def clientlistall(request):
	allclients = Client.objects.all()
	client_list = {"clients" : allclients}	
	template = "client_list.html"
	return render_to_response(template, client_list)
	
@login_required
def clientvisit(request):
	form = ClientVisitForm(request.POST or None)
	searchform = SearchForm(request.POST or None)
	if form.is_valid():
		save_it = form.save(commit=False)
		save_it.save()
	
	context = {"form" : form, 'searchform' : searchform}
	template = "fpcard.html"
	return render(request, template, context)

def search(request):
	if request.method == "POST":
		search_text = request.POST['search_text']	
	else:
		search_text = ''

	clients = Client.objects.filter(firstName__contains=search_text)
	template = "test.html"
	return render(request, template, {'clients' : clients})

def singleclient(request, clientId):
	form = ClientVisitForm()
	#if request.method == "GET":
	#	client_code = request.GET['clientcode']
	if clientId:
		clients = Client.objects.get(code=clientId)
		clientVisitHistory = ClientVisit.objects.filter(clientCode=clientId)
	
	return render(request, 'clienthistory.html', {'clients' : clients,'clientVisitHistory':clientVisitHistory, 'form': form})

def addrecord(request,clientId):

	if request.is_ajax():
		if request.method == "POST":
			#client = Client.objects.get(code=clientId)
			#client = Client.objects.get(code=clientId)
			#clientVisit = ClientVisit(instance=client)
			#print("***"+client.code)
			submittedClientVisitForm = ClientVisitForm(request.POST or None)
			#print(submittedClientVisitForm['clientCode'])
			if submittedClientVisitForm.is_valid():
				dateSeen = datetime.strptime(str(submittedClientVisitForm.cleaned_data['dateSeen']), "%Y-%m-%d")
				dateFollowUp = datetime.strptime(str(submittedClientVisitForm.cleaned_data['followUpDate']), "%Y-%m-%d")
				save_ClientVisit = submittedClientVisitForm.save(commit=False)
				clients = Client.objects.get(code=clientId)
				save_ClientVisit.clientCode = clients
				save_ClientVisit.dateSeen = dateSeen
				save_ClientVisit.followUpDate = dateFollowUp
				save_ClientVisit.save()
				submittedClientVisitForm.save_m2m()
			else:
				print("error in form")
	else:
		print("No ajax call")
	return render(request, 'addrecord.html')