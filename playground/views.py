from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# request => response


def say_hello(http_request):
    return HttpResponse("hola mundo")
