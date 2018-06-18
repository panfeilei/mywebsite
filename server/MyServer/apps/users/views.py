import random

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

from apps.blogs.models import Blog
from apps.blogs.models import getFileDict
from .models import MyUser
from .serializers import UserMsgSerializer, SysMsgSerializer

from apps.blogs.serializers import BlogMsgSerializer
from apps.users.models import UserInfo
from .models import SystemMessage, UserMessage
from apps.blogs.models import BlogMessage

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

def handleMessage(msg):
    pass

def getMessage(request):
    userId = request.user.userId
    response = {}
    user = UserInfo.objects.get(userId=userId)
    blgMsg = BlogMessage.objects.filter(toUser=user, isRead=False)
    sysMsg = SystemMessage.objects.filter(toUser=user, isRead=False)
    usrMsg = UserMessage.objects.filter(toUser=user, isRead=False)
    response["all"] = len(sysMsg) + len(blgMsg) + len(usrMsg)
    response["comment"] = str(len(blgMsg))
    response["letter"] = str(len(usrMsg))
    response['interest'] = str(len(usrMsg.filter(msgType='INT')))
    response["sys"] = str(len(sysMsg))
    return JsonResponse(response)

def getMessageInfo(request):
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

class BlogMsgViewSet(viewsets.ModelViewSet):
    serializer_class = BlogMsgSerializer
    queryset = BlogMessage.objects.all()
    lookup_field = 'toUser'

class AllMsgViewSet(viewsets.GenericViewSet):

    def list(self, request, *args, **kwargs):
        uerid = request.user.userId
        blogQuerySet = BlogMessage.objects.filter(toUser=uerid)
        userQuerySet = UserMessage.objects.filter(toUser=uerid)
        sysQuerySet = SystemMessage.objects.filter(toUser=uerid)
        blogSerializer = BlogMsgSerializer(blogQuerySet, many=True)
        userSerializer = UserMsgSerializer(userQuerySet, many=True)
        sysSerializer = SysMsgSerializer(sysQuerySet, many=True)
        resp = {'blog': blogSerializer.data,
                'user': userSerializer.data,
                'sys': sysSerializer.data}

        return Response(resp)

