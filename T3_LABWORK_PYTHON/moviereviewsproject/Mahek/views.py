from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def name(request):
    return HttpResponse("<h1>Name:Mahek Koshti <br> Enrollment no:24002171310064 <br></h1>")