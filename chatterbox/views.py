from django.shortcuts import render, HttpResponse


# sem budeme pridavat

# Create your views here.

def hello(request):
    return HttpResponse("HELLO WORLD!!!")