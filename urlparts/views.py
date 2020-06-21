from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def index(request, path):
    pathvariables = path.split('/')
    if '//' in path or pathvariables[0] == '':
        return HttpResponse("Ongeldige url")
    return render(request, 'urlparts/index.html', {'parts': pathvariables})