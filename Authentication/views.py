from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'Authentication/SignUp.html')

def signUpSubmit(request):
    fname=request.POST['fname']
    print(fname)
    return HttpResponse(fname)
