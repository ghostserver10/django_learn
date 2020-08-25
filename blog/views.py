from django.shortcuts import render
from django.http import HttpResponse


def home(render):
    return HttpResponse('<h1>Blog home</h1>')

def about(render):
    return HttpResponse('<h1>Blog about</h1>')    
