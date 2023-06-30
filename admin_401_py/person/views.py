from http.client import HTTPResponse
from django.shortcuts import render

from person.models import Person

# Create your views here.
def index(request):
    print('aca person')