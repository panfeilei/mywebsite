from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    
    return render(request, 'login.html')
    
def testpost(request):
    print("get user"+request.GET.get('user', ''))
    return HttpResponse('logintest')