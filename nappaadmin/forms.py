#!/usr/bin/env python3
from nappaadmin import models as m
from django.forms import ModelForm

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