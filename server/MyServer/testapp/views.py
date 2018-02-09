from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.
class dd():
    f=4
def login(request):
    print("get login")
    username=request.GET.get('user')
    password=request.GET.get('pwd')
    user=authenticate(username=username, password=password)
    if user is not None:
        return HttpResponse("login success");
    else:
        return render(request, 'login.html')
    
def testpost(request):
    #print("get user"+request.GET.get('user', ''))
    return HttpResponse('logindddtest')
    
def index(request):
    return render(request, 'index.html')