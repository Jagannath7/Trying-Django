from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Hello World')

def name(request):
    return render(request, 'name.html',{'name':'Jagannath'})