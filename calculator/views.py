from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request): 
    return HttpResponse("Hello, Santeri. Welcome to your future RO calculator app.")