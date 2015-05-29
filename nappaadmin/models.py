#!/usr/bin/env python3
from django.db import models

# Create your models here.
SEX_CHOICES = (
    ('M', 'M'),
    ('F', 'F'),
    ('T', 'T'),
)

MARITAL_STATUS = (
('1', 'Single'),
('2', 'Married'),
('3', 'Widow/widower'),
('4', 'Divorce/Separate'),
)

HEALTH_BOOK = (
('Y', 'Y'),
('N', 'N'),
)

class Facility(models.Model):
	code = models.CharField(max_length=12, primary_key=True)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=30)
	telephone = models.IntegerField()
	active = models.BooleanField(default=False)
	address = models.CharField(max_length=50)
	createdDate = models.DateTimeField(auto_now_add = True, auto_now = False)
	updatedDate = models.DateTimeField(auto_now_add = False, auto_now = True)
	
	def __unicode__(self):
		return "%s" %(self.code + " "+self.name)
		
class Client(models.Model):
	code = models.CharField(max_length=12, primary_key=True)
	firstName = models.CharField(max_length=30)
	lastName = models.CharField(max_length=30)
	registeredDate = models.DateTimeField(auto_now_add = True, auto_now = False)
	sex = models.CharField(max_length=1, choices=SEX_CHOICES, default = "F")
	age = models.IntegerField(default=0)
	maritalStatus = models.CharField(max_length=1, choices=MARITAL_STATUS, default = "1")
	healthBook = models.CharField(max_length=1, choices=HEALTH_BOOK, default = "Y")
	referral =  models.CharField(max_length=30)
	
	def __unicode__(self):
		return "%s" %(self.code)
		
class Service(models.Model):
	code = models.CharField(max_length=12, primary_key=True)
	name = models.CharField(max_length=30)
	abbreviation = models.CharField(max_length=4)
	
	def __unicode__(self):
		return "%s" %(self.code)

class ServiceReceived(models.Model):
	clientCode = models.ForeignKey(Client)
	facilityCode = models.ForeignKey(Facility)
	serviceCode = models.ForeignKey(Service)
	
	def __unicode__(self):
		return "%s" %(self.clientCode)