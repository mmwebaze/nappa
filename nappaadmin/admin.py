#!/usr/bin/env python3
from django.contrib import admin
from django import forms
from nappaadmin.models import Facility
from nappaadmin.models import Client
from .models import Service, ServiceReceived, ClientVisit

class FacilityAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'code', 'name', 'description']
	class Meta:
		model = Facility

class ClientAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'registeredDate','code', 'firstName','lastName', 'sex', 'age','maritalStatus','healthBook','referral']
	class Meta:
		model = Client
		
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'code', 'name', 'abbreviation']
	class Meta:
		model = Service

class ServiceReceivedAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'clientCode', 'facilityCode', 'serviceCode']
	class Meta:
		model = ServiceReceived

class ClientVisitForm(forms.ModelForm):
	comments = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = ClientVisit
		fields = "__all__" 

class ClientVisitAdmin(admin.ModelAdmin):
	form = ClientVisitForm

		# Register your models here.
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceReceived, ServiceReceivedAdmin)
admin.site.register(ClientVisit, ClientVisitAdmin)