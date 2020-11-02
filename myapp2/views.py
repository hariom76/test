from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<body><h1>hows your girlfriend</h1><b>fuck off my girlfriend</b> </body>')
