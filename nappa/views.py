#!/usr/bin/env python3
from django.shortcuts import render

def home(request):
	context = {}
	template = "home.html"
	return render(request, template, context)