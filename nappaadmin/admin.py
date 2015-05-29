#!/usr/bin/env python3
from django.contrib import admin
from nappaadmin.models import Facility
from nappaadmin.models import Client
from .models import Service, ServiceReceived

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

		# Register your models here.
admin.site.register(Facility, FacilityAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceReceived, ServiceReceivedAdmin)