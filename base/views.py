from django.shortcuts import render,redirect

def login(request):
    context={}
    return render(request,"login.html",context)
