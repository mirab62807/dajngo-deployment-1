from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request):
   return  HttpResponse("Got it from httpresponse")


def about(response):
   return HttpResponse("I am Abdullah and trying to learn to cope")

def hello(request, fn):
   return HttpResponse(f"hello {fn}")

def add(request, n1, n2):
   s = n1+n2 
   return HttpResponse(f" sum of the numbers {s}")


