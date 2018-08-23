import json
import os
import time

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.response import Response
from django.views import View
from django.shortcuts import get_list_or_404
from django.db.models import F
import django_filters

from apps.blogs.models import Blog
from apps.blogs.models import Comment, Reply, Category
from apps.blogs.models import testmedel
from apps.users.models import MyUser, UserInfo
from .serializers import BlogSerializer, CommentSerializer, ReplySerializer, testModelSerializer
from apps.operation.models import Favorite, Interest
from apps.blogs.models import BlogMessage
from apps.users.serializers import UserInfoSerializer
MEDIA_PATH = settings.MEDIA_ROOT


class BlogFilter(django_filters.FilterSet):
    key = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = {'title', 'content'}


def serachblog(request):
    result = BlogFilter(request.GET)
    key = request.GET['key']

    for b in result.qs:
        print(type(b.time))
        return render(request, 'search.html', {'filter': result, 'key': key})

def mylogin(request):
    print("get login")
    username = request.GET.get('user')
    password = request.GET.get('pwd')
    u = request.user
    print(request.user.id)
    print('ttt')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login.html', context={'loginStatus': 'True'})
    else:
        return render(request, 'login.html', context={'loginStatus': 'False'})


def testpost(request):
    #print("get user"+request.GET.get('user', ''))
    t = testmedel()
    print("get user")
    return render(request, 'test.html', {'testfiled': t})


def editor(request):
    categoryList = Category.objects.all()
    return render(request, 'editor.html', {'categoryList': categoryList})


def blog_view(request, id):
    blogs = Blog.objects.filter(blogId=id)
    #print(type(blogs[0].authorId.UserInfo))
    #print(blogs[0].authorId.inter_list.count())
    blogs.update(readNum=F('readNum')+1)
    blogfrom = request.GET.get('from')
    if blogfrom == 'message':
        b = BlogMessage.objects.filter(blog=blogs[0])
        b.update(isRead=True)
    return render(request, 'blog.html', {'Blog': blogs[0]})


def testView(request):
    return render(request, 'search.html')


@csrf_exempt
def uploadIcon(request):
    print(request.FILES)
    print(settings.MEDIA_ROOT)
    icon = request.FILES['icon-image']
    with open(os.path.join(MEDIA_PATH, request.user.username + "-icon.jpg"), 'wb+') as f:
        for chunk in icon.chunks():
            f.write(chunk)
            user = UserInfo.objects.get(userId=request.user.userId)
            user.iconUrl = '/media/'+request.user.username + '-icon.jpg'
            user.save()
    return HttpResponse('upload ok')


def test1(request):
    return render(request, 'search.html')


@csrf_exempt
def uploadData(request):
    action = request.GET.get('action')
    user = request.user
    if not user.is_authenticated:
        print('no login')
        return HttpResponse('no login')
    if action == "uploadBlog":
        now = time.time()
        title = request.POST.get('title')
        content = request.POST.get('content')
        descript = request.POST.get('descript')
        autor = UserInfo.objects.get(userId=user.userId)
        cate = Category.objects.get(categoryId=request.POST.get('category'))
        blogId = str(hash(str(now) + title)).replace('-', '')
        link = "/blog/%s" % (blogId)
        b = Blog(title=title, content=content, link=link,
                 descript=descript, blogId=blogId, authorId=user, category=cate)
        b.save()
    elif action == "uploadComment":
        content = request.POST.get('content')
        to_blogId = request.POST.get('to_blogId')
        b = Blog.objects.get(blogId=to_blogId)
        userId = request.user.userId
        userInfo = UserInfo.objects.get(userId=userId)
        authoruserInfo = UserInfo.objects.get(userId=request.user)
        name = request.user.username
        c = Comment(content=content,
                    to_blogId=b,
                    name=name,
                    userInfo=userInfo)
        c.save()
        msg = BlogMessage(msgType='CO', user=userInfo, blog=b, toUser=authoruserInfo)
        msg.save()

    elif action == "uploadReply":
        content = request.POST.get('content')
        to_blogId = request.POST.get('toblogId')
        to_commentId = request.POST.get('toCommentId')
        to_username = request.POST.get('toUsername')
        userInfo = UserInfo.objects.get(userId=request.user.userId)
        c = Comment.objects.get(comment_id=to_commentId)
        r = Reply(content=content, to_blogId=to_blogId,
                  to_commentId=c, userInfo=userInfo, to_username=to_username)
        r.save()
    return HttpResponse('ok')


def mylogout(request):
    user = request.user
    if user:
        print('user logout')
        logout(request)
        return redirect('login')
    else:
        return HttpResponse('not user')


@login_required
def index(request, module):
    currentCategory = None
    if len(module) == 0:
        return HttpResponseRedirect('/index/new/')
    if module == 'new':
        blogs = Blog.objects.all()
    else:
        currentCategory = Category.objects.get(value=module)
        blogs = Blog.objects.filter(category=currentCategory)
    category = Category.objects.all()
    #print(blogs[0].category.value)
    context = {'category':category, 'isAll': currentCategory==None}
    if blogs:
        #blog_list = BlogSerializer(blogs, many=True)
        context['blog_list']= blogs
    return render(request, 'index.html', context)


def defaulInex(request):
    return HttpResponseRedirect(reverse('index', args=['']))


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'blogId'


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'to_blogId'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, many=True)
        return Response(serializer.data)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_list_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)
        return obj


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = testmedel.objects.all()
    serializer_class = testModelSerializer


class testViewSet(viewsets.ModelViewSet):
    queryset = testmedel.objects.all()
    serializer_class = testModelSerializer


class BlogInfo(View):

    def get(self, request, blogId):
        resp = {}
        user = request.user
        fav = Favorite.objects.filter(blogId=blogId)
        isfav = fav.filter(user=user.userId)
        blog = Blog.objects.get(blogId=blogId)
        #author = MyUser.objects.get(UserInfo=blog.authorId) #反查
        author = blog.authorId
        authorInfo = UserInfo.objects.get(userId=author)
        userinfo = UserInfoSerializer(authorInfo)
        BlogNum = Blog.objects.filter(authorId=blog.authorId)
        inter = Interest.objects.filter(Q(toUserId=author), Q(user=user))
        print(userinfo.data)
        resp['blogInfo'] = {'favorNum': len(fav), 'isFavou': len(isfav) > 0}
        resp['authorInfo'] = {'BlogNum': len(BlogNum), 'UserInfo': userinfo.data, 'isIntere': len(inter) > 0}
        print(str(resp))
        return JsonResponse(resp)
