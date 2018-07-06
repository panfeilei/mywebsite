import random
from functools import reduce

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics

from apps.blogs.models import Blog, Comment
from apps.blogs.models import getFileDict
from .models import MyUser
from .serializers import UserMsgSerializer, SysMsgSerializer
from apps.blogs.serializers import BlogMsgSerializer, BlogSerializer
from apps.users.models import UserInfo
from .models import SystemMessage, UserMessage
from apps.blogs.models import BlogMessage
from apps.operation.models import Interest,Favorite

def UserInfoWrapper(func):
    def _wrapper(request, **kw):
        Context = {}
        u = UserInfo.objects.filter(userId=request.user)
        if len(u) == 0:
            print('user is none')
            return HttpResponse("user is none")
        else:
            fans = Interest.objects.filter(toUserId=request.user)
            Context['userinfo'] = u[0]
            Context['fans'] = fans
            return func(request, **kw, Context=Context)
    return _wrapper

@UserInfoWrapper
def home(request, userId, Context):
    visitor = request.user.userId
    b = Blog.objects.filter(authorId=userId)
    blogList = BlogSerializer(b, many=True)
    comment = Comment.objects.filter(userInfo=Context['userinfo'])
    Context['commentsize']= len(comment)
    Context['bloglist'] = blogList.data
    Context['isVisitor'] = int(userId) != visitor
    return render(request, 'users/user-home.html',Context)

@UserInfoWrapper
def MyFavourite(request, Context):
    myFav = Favorite.objects.filter(user=request.user)
    Context['myFavourite'] = myFav
    return render(request, 'users/user-favourite.html', Context)

def countQuery(item1, item2):
    return len(item1)+len(item2)

def getMessage(request):
    userId = request.user.userId
    response = {}
    user = UserInfo.objects.get(userId=userId)
    blgMsg = BlogMessage.objects.filter(toUser=user, isRead=False)
    sysMsg = SystemMessage.objects.filter(toUser=user, isRead=False)
    usrMsg = UserMessage.objects.filter(toUser=user, isRead=False)
    inte = Interest.objects.filter(user=request.user)
    tt = [Blog.objects.filter(authorId=i.toUserId.UserInfo, time__gt=i.time) for i in inte]
    interest = 0
    if len(tt)>0:
        interest = reduce(countQuery, tt)
    response["all"] = len(sysMsg) + len(blgMsg) + len(usrMsg) + interest
    response["comment"] = str(len(blgMsg))
    response["letter"] = str(len(usrMsg.filter(msgType='LE')))
    response['interest'] = interest
    response["sys"] = str(len(sysMsg))
    response["fans"] = str(len(usrMsg.filter(msgType='INT')))
    return JsonResponse(response)

@UserInfoWrapper
def follower(request, Context):
    userId = request.user.userId
    u = UserInfo.objects.filter(userId=userId)
    inte = Interest.objects.filter(user=request.user)
    tt = [Blog.objects.filter(authorId=i.toUserId.UserInfo, time__gt=i.time) for i in inte]
    data = [BlogSerializer(t, many=True) for t in tt]
    for d in data:
        print(d.data)
    comment = Comment.objects.filter(userInfo=u[0])
    return render(request, 'users/user-follower.html',
                    {'userinfo':u[0],
                     'commentsize': len(comment),
                     'followerBlog':tt})

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
            u = UserInfo(name=username, userId=user)
            u.save()
            return render(request, 'apply.html',context={'applyStatus':'True'})
        else:
            print("apply error")
            return HttpResponse("apply register error")

class BlogMsgViewSet(viewsets.ModelViewSet):
    serializer_class = BlogMsgSerializer
    queryset = BlogMessage.objects.all()
    lookup_field = 'toUser'

class UserMsgViewSet(viewsets.ModelViewSet):
    serializer_class = UserMsgSerializer
    queryset = UserMessage.objects.all()
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

