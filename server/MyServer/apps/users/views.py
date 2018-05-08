from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import MyUser,Blog
from apps.users.models import UserInfo, UnreadMessage, Message
import random
def home(request, userId):
    print(userId)
    u = UserInfo.objects.filter(userId=userId)
    if len(u) == 0:
        print('user is none')
        return HttpResponse("user is none")
    else:
        blogList = Blog.objects.filter(author=userId)
        print('user icon' + u[0].iconUrl)
        return render(request, 'user-home.html', {'userinfo':u[0], 'bloglist':blogList})

def addMessage(name, userId, content, toUserId, type):
    m = UnreadMessage(name=name, userId=userId, content=content, toUserId=toUserId, type=type)
    m.save()

def handleMessage(msg):
    pass

def apply(request):
    if len(request.GET) == 0:
        return render(request, 'apply.html',context={'applyStatus':'False'})
    else:
        username=request.GET.get('user')
        password=request.GET.get('pwd')
        repeatpwd = request.GET.get('repwd')
        email = request.GET.get('email')
        id = -1
        while(id == -1):
            id = random.randint(1,255)
            uu = MyUser.objects.filter(userId = id)
            if uu:
                id = -1
        user = MyUser.objects.create_user(username, email, password, userId=id)
        print(user)
        if user:
            u = UserInfo(name=username, userId=id)
            u.save()
            return render(request, 'apply.html',context={'applyStatus':'True'})
        else:
            print("apply error")
            return HttpResponse("apply register error")