from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

async def home(request:HttpRequest) -> HttpResponse:
   return render (request, 'account/home.html', {'x':33})

def register(request:HttpRequest) -> HttpResponse:
   return render (request, 'account/register.html')
    

def login(request:HttpRequest) -> HttpResponse:
   return render (request, 'account/login.html')
