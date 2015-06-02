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
		fields = ('code', 'firstName','lastName', 'sex', 'age','maritalStatus','healthBook','referral')
		
class ServiceForm(ModelForm):
	class Meta:
		model = m.Service
		fields = ('code', 'name','abbreviation')
		
class ServiceReceivedForm(ModelForm):
	class Meta:
		model = m.ServiceReceived
		fields = ('clientCode', 'facilityCode','serviceCode')

class FamilyPlanningCardForm(ModelForm):
	dateSeen = forms.DateField(widget=DateInput())
	followUpDate = forms.DateField(widget=DateInput())
	comments = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = m.FamilyPlanningCard
		fields = "__all__" 

class SearchForm(forms.Form):
	message = forms.CharField(max_length=15)