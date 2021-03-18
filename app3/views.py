from django.shortcuts import render

# Create your views here.
from django.http  import HttpResponse

def hi(request):
    return HttpResponse('rehmani is good guy')
def by(request):
    return HttpResponse('<h1 style="color:red"><marquee>rehmani is a good guy</marquee></h1>')