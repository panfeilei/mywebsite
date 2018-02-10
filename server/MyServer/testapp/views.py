from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext,Template
# Create your views here.
class dd():
    f=4


def mylogin(request):
    #print("get login")
    username=request.GET.get('user')
    password=request.GET.get('pwd')
    u=request.user
    print(request.user.id)
    print('ttt')
    user=authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login.html',context={'loginStatus':'True'})
    else:
        return render(request, 'login.html', context={'loginStatus':'False'})

def testpost(request):
    #print("get user"+request.GET.get('user', ''))
    return HttpResponse('logindddtest')
def editor(request):
    return render(request, 'editor.html')

@login_required
def index(request):
    #t=Template('index.html')
    c = RequestContext(request, {
        'foo': 'bar',
    })
    #return HttpResponse(t.render(c))
    return render(request, 'index.html')