import random

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from apps.blogs.models import MyUser,Blog
from apps.blogs.models import getFileDict
from apps.users.models import UserInfo, UnreadMessage as Unread, Message


def home(request):
    userId = request.user.userId
    print(userId)
    u = UserInfo.objects.filter(userId=userId)
    if len(u) == 0:
        print('user is none')
        return HttpResponse("user is none")
    else:
        blogList = Blog.objects.filter(authorId=userId)
        print('user icon' + u[0].iconUrl)
        return render(request, 'users/user-home.html', {'userinfo':u[0], 'bloglist':blogList})

def addMessage(name, userId, content, toUserId, type, fromBlog, link):
    m = Unread(name=name, userId=userId, content=content,
               toUserId=toUserId, type=type, fromBlog=fromBlog,
               link=link)
    m.save()

def handleMessage(msg):
    pass

def getMessage(request):
    userId = request.user.userId
    response = {}
    print(userId)
    allMessage = Unread.objects.filter(toUserId=userId)
    response["all"] = len(allMessage)
    response["comment"] = str(len(allMessage.filter(type="comment")))
    response["letter"] = str(len(allMessage.filter(type="letter")))
    return JsonResponse(response)

def getMessageInfo(request):
    type = request.GET.get('type')
    userId = request.user.userId
    message={}
    if type == 'comment':
        unr = Unread.objects.filter(toUserId=userId, type=type)
        read = Message.objects.filter(toUserId=userId, type=type)
        readList = []
        unreadList = []
        for r in read:
            d = getFileDict(r)
            readList.append(d)
        message['read'] = readList
        for u in unr:
            d = getFileDict(u)
            unreadList.append(d)
            m = Message.objects.createMessage(u)
            m.save()
        unr.delete()
        message['unread'] = unreadList
        return JsonResponse(message)
    elif type == 'letter':
        pass
    return render(request, 'users/user-msg.html')

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