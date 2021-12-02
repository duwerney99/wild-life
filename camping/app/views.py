from django.http.response import HttpResponse
from django.shortcuts import render

def Index(request):
    return HttpResponse('Hello World.')