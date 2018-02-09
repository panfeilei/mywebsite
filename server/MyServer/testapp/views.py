from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
class dd():
    f=4
def login(request):
    print("get login")
    d=dd()
    return render(request, 'login.html',context={'foo':d})
    
def testpost(request):
    #print("get user"+request.GET.get('user', ''))
    return HttpResponse('logindddtest')
    
def index(request):
    return render(request, 'index.html')