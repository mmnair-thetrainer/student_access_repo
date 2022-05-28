from django.http import response
from django.shortcuts import render
def home(request):
    # return response.HttpResponse("<h1>hello</h1>")
    return render(request,'home.html')
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'hanna'
    
    
    })
