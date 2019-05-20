from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.http import FileResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


def index(request):
    return render(request,'index.html')

def results(request):
	return render(request,'results.html')

def text(request, resultid):
	return render(request,'text.html', {'resultid':resultid})

def words(request, resultid):
	return render(request,'words.html', {'resultid':resultid})