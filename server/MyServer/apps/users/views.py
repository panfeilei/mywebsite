import random
from functools import reduce

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_list_or_404
from rest_framework import viewsets
from django.db.models import F
from django.utils.timezone import now
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
        context = {}
        u = UserInfo.objects.filter(userId=request.user)
        if len(u) == 0:
            print('user is none')
            return HttpResponse("user is none")
        else:
            fans = Interest.objects.filter(toUserId=request.user)
            context['userinfo'] = u[0]
            context['fans'] = fans
            return func(request, **kw, Context=context)
    return _wrapper


@UserInfoWrapper
def home(request, userId, context):
    visitor = request.user.userId
    b = Blog.objects.filter(authorId=userId)
    blogList = BlogSerializer(b, many=True)
    comment = Comment.objects.filter(userInfo=context['userinfo'])
    context['commentsize'] = len(comment)
    context['bloglist'] = blogList.data
    context['isVisitor'] = int(userId) != visitor
    return render(request, 'users/user-home.html',context)


@UserInfoWrapper
def MyFavourite(request, context):
    myFav = Favorite.objects.filter(user=request.user)
    context['myFavourite'] = myFav
    return render(request, 'users/user-favourite.html', context)


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
    tt = [Blog.objects.filter(authorId=i.toUserId, time__gt=i.lastCheckTime) for i in inte]
    interest = 0
    if len(tt)>2:
        interest = reduce(countQuery, tt)
    elif len(tt) == 1:
        interest = len(tt[0])
    response["all"] = len(sysMsg) + len(blgMsg) + len(usrMsg) + interest
    response["comment"] = str(len(blgMsg))
    response["letter"] = str(len(usrMsg.filter(msgType='LE')))
    response['interest'] = interest
    response["sys"] = str(len(sysMsg))
    response["fans"] = str(len(usrMsg.filter(msgType='INT')))
    return JsonResponse(response)


@UserInfoWrapper
def follower(request, context):
    inte = Interest.objects.filter(user=request.user)
    print('update interest')
    tt = [Blog.objects.filter(authorId=i.toUserId, time__gt=i.time) for i in inte]
    myInterest = list(filter(len, tt))
    comment = Comment.objects.filter(userInfo=context['userinfo'])
    context['commentsize'] = len(comment)
    context['followerBlog'] = myInterest
    inte.update(lastCheckTime=now())
    print(myInterest)
    return render(request, 'users/user-follower.html', context)


def getMessageInfo(request):
    return render(request, 'users/user-msg.html')


def apply(request):
    if len(request.GET) == 0:
        return render(request, 'apply.html',context={'applyStatus':'False'})
    else:
        username = request.GET.get('user')
        password = request.GET.get('pwd')
        repeatpwd = request.GET.get('repwd')
        email = request.GET.get('email')
        id = -1
        while id == -1:
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

