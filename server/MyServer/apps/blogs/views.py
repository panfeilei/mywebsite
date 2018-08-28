import json
import os
import time
import random
import string
from io import BytesIO

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
from PIL import Image, ImageDraw, ImageFont
import django_filters
from django.core.cache import cache
from django.http import StreamingHttpResponse

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

@csrf_exempt
def download(request):
    def file_iterator(file_name, chunk_size=2048):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    filename = request.GET['file']
    print(filename)
    response = StreamingHttpResponse(file_iterator('media/download/{0}'.format(filename)))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="{0}"'.format(filename)
    return response


def serachblog(request):
    result = BlogFilter(request.GET)
    key = request.GET['key']

    for b in result.qs:
        print(type(b.time))
        return render(request, 'search.html', {'filter': result, 'key': key})


def getRandomStr():
    '''获取一个随机字符串，每个字符的颜色也是随机的'''
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
    return random_char


def getRandomColor():
    c1 = random.randint(0, 250)
    c2 = random.randint(0, 250)
    c3 = random.randint(0, 250)
    return c1, c2, c3


def create_code_img(request):
    image = Image.new('RGB', (100, 20), (216, 216, 220))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("C:\Windows\Fonts\Corbel.ttf", size=16)
    key = ''
    cache.delete(request.GET['key']+'.jpg')
    for i in range(4):
        random_char = getRandomStr()
        key += random_char
        draw.text((10 + i * 20, 0), random_char, getRandomColor(), font=font)
    cache.set(request.GET['key'], key.lower())
    f = BytesIO()
    image.save(f, 'jpeg')
    cache.set(request.GET['key']+'.jpg', f.getvalue())
    f.close()
    return HttpResponse(cache.get(request.GET['key']+'.jpg'), 'image/jpeg')


def verify(request):
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    captchCode = request.POST.get('captcha')
    if cache.get(request.POST['captch_key']) != captchCode.lower():
        return loginView(request, '验证码错误')
        #return redirect('/login/?warning=captch')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        return loginView(request, '账号密码错误')
        #return redirect('/login/?warning=account')
    return loginView(request)


def loginView(request, warning=''):
    captchKey = ''
    #warningDict = {'captch': '验证码错误', 'account': '账号密码错误'}
    #warningKey = request.GET.get('warning', '')
    #warningText = warningDict.get(warningKey, '')
    #print(warningKey)
    for i in range(5):
        captchKey += random.choice(string.ascii_letters)
    if request.user.is_authenticated:
        status = 'True'
    else:
        status = 'False'
    return render(request, 'login.html', context={'loginStatus': status, 'captchKey': captchKey, 'warning': warning})


def testpost(request):
    t = testmedel()
    print("get user")
    return render(request, 'test.html', {'testfiled': t})


def editor(request):
    categoryList = Category.objects.all()
    return render(request, 'editor.html', {'categoryList': categoryList})


def blog_view(request, id):
    blogs = Blog.objects.filter(blogId=id)
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
