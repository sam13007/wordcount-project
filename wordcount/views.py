from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    
    text=request.GET['text']
    full=text.split()
    return render(request,'count.html',{'name':'shyam','text':text,'len':len(full)})