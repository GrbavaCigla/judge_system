from django.shortcuts import render, HttpResponse

# Create your views here.
def home():
    return HttpResponse("<h1>Works</h1>")