from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1> Yo soy kaka </h1>")

def help(request):
    helpdict={'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)