#!/usr/bin/env python3
from nappaadmin import models as m
from django.forms import ModelForm
from django import forms
from functools import partial

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class FacilityForm(ModelForm):
	class Meta:
		model = m.Facility
		fields = ('code', 'name','description','telephone','active','address')
	
class ClientForm(ModelForm):
	class Meta:
		model = m.Client
		#fields = ('code', 'firstName','lastName', 'sex', 'age','maritalStatus','healthBook','referral')
		fields = "__all__"
		
class ServiceForm(ModelForm):
	class Meta:
		model = m.Service
		fields = ('code', 'name','abbreviation')
		
class ServiceReceivedForm(ModelForm):
	class Meta:
		model = m.ServiceReceived
		fields = ('clientCode', 'facilityCode','serviceCode')

class ClientVisitForm(ModelForm):
	dateSeen = forms.DateField(widget=DateInput())
	followUpDate = forms.DateField(widget=DateInput())
	comments = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
	
	class Meta:
		model = m.ClientVisit
		fields = ('method', 'bp', 'weight','lnmp','comments')
		exclude = ('clientCode',)

class SearchForm(forms.Form):
	clientcode = forms.CharField(max_length=100)