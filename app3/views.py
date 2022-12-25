from django.shortcuts import render
from django.http import HttpResponse

def varsha(request):
    return HttpResponse('<h1> you are my love</h1>')


def manvi(request):
    return HttpResponse('<marquee><h1> you are beautiful </h1></marquee>')
