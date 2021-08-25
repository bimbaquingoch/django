from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# request => response


def say_hello(http_request):
    return render(
        http_request,
        "hello.html",
        {
            "name": "Giorno",
        },
    )
