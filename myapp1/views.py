from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hey there i m')
def hariom(request):
   return render(request,'myapp/django.html')