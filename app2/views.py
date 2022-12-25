from django.shortcuts import render
from django.http import HttpResponse

def tarun(request):
    return HttpResponse('<h1>i am a good boy</h1>')
def manoj(request):
    return HttpResponse('<h1><marquee> congratulations</marquee></h1>')
