from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.
def teste(request):
    return HttpResponse("<p>ok</p>")