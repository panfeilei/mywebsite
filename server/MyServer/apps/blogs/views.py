import json
import os
import time

from django.conf import settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template import RequestContext,Template,loader
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from rest_framework import viewsets
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.views import View
from django.shortcuts import get_list_or_404
from django import template
from django.db.models import F

from apps.blogs.models import  Blog
from apps.blogs.models import  Comment, Reply
from apps.blogs.models import testmedel
from apps.users.models import UserInfo
from apps.users.models import MyUser
from .serializers import BlogSerializer,CommentSerializer, ReplySerializer,testModelSerializer
from apps.operation.models import Favorite, Interest
from apps.blogs.models import BlogMessage
from apps.users.serializers import UserInfoSerializer
MEDIA_PATH = settings.MEDIA_ROOT

# Create your views here.

def mylogin(request):
    print("get login")
    username=request.GET.get('user')
    password=request.GET.get('pwd')
    u=request.user
    print(request.user.id)
    print('ttt')
    user=authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'login.html', context={'loginStatus': 'True'})
    else:
        return render(request, 'login.html', context={'loginStatus': 'False'})

def testpost(request):
    #print("get user"+request.GET.get('user', ''))
    t = testmedel()
    print("get user")
    return render(request, 'test.html', {'testfiled':t})

def editor(request):
    return render(request, 'editor.html')

def blog_view(request,id):
    blogs = Blog.objects.filter(blogId=id)
    blogs.update(readNum = F('readNum')+1)
    blogfrom=request.GET.get('from')
    if blogfrom == 'message':
        b = BlogMessage.objects.filter(blog=blogs[0])
        b.update(isRead =True)
    return render(request, 'blog.html', {'Blog':blogs[0]})
    
def testView(request):
    return render(request, 'test.html')

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
    return render(request, 'test1.html')

@csrf_exempt
def test(request):
    print(request.GET)
    action = request.GET.get('action')
    print(action)
    if request.method == 'POST':

        if action == 'uploadimage':
            img = request.FILES.get('upfile')
            print(request.FILES)
            #print(img)
            #print(settings.MEDIA_ROOT)
            imgt = open(settings.MEDIA_ROOT+"\\"+img.name, "wb+")
            for l in img.chunks():
                imgt.write(l)
            imgt.close()
            return HttpResponse('{"state": "SUCCESS","url": "http://127.0.0.1:8000/media/%s","title": "dem_title.jpg", "original": "demo_original.jpg"}' %img.name )
    t = Template(r'{"imageActionName":"uploadimage","imageFieldName":"upfile","imageMaxSize":2048000,"imageAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"imageCompressEnable":true,"imageCompressBorder":1600,"imageInsertAlign":"none","imageUrlPrefix":"","imagePathFormat":"/upload/{filename}","scrawlActionName":"uploadscrawl","scrawlFieldName":"upfile","scrawlPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","scrawlMaxSize":2048000,"scrawlUrlPrefix":"","scrawlInsertAlign":"none","snapscreenActionName":"uploadimage","snapscreenPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","snapscreenUrlPrefix":"","snapscreenInsertAlign":"none","catcherLocalDomain":["127.0.0.1","localhost","img.baidu.com"],"catcherActionName":"catchimage","catcherFieldName":"source","catcherPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","catcherUrlPrefix":"","catcherMaxSize":2048000,"catcherAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"videoActionName":"uploadvideo","videoFieldName":"upfile","videoPathFormat":"\/server\/ueditor\/upload\/video\/{yyyy}{mm}{dd}\/{time}{rand:6}","videoUrlPrefix":"","videoMaxSize":102400000,"videoAllowFiles":[".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid"],"fileActionName":"uploadfile","fileFieldName":"upfile","filePathFormat":"\/server\/ueditor\/upload\/file\/{yyyy}{mm}{dd}\/{time}{rand:6}","fileUrlPrefix":"","fileMaxSize":51200000,"fileAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp",".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid",".rar",".zip",".tar",".gz",".7z",".bz2",".cab",".iso",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".txt",".md",".xml"],"imageManagerActionName":"listimage","imageManagerListPath":"\/server\/ueditor\/upload\/image\/","imageManagerListSize":20,"imageManagerUrlPrefix":"","imageManagerInsertAlign":"none","imageManagerAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"fileManagerActionName":"listfile","fileManagerListPath":"\/server\/ueditor\/upload\/file\/","fileManagerUrlPrefix":"","fileManagerListSize":20,"fileManagerAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp",".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid",".rar",".zip",".tar",".gz",".7z",".bz2",".cab",".iso",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".txt",".md",".xml"]}')
    req = RequestContext(request)
    return HttpResponse(t.render(req))
    
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
        blog_id = str(hash(str(now) + title)).replace('-', '')
        link = "http://127.0.0.1:8000/blog/%s" %  (blog_id)
        b = Blog(title=title, content=content, link=link,
                 descript=descript, blogId=blog_id, authorId=autor)
        b.save()
    elif action == "uploadComment":
        
        content = request.POST.get('content')
        to_blogId = request.POST.get('to_blogId')
        b = Blog.objects.get(blogId = to_blogId)
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
def index(request):
    request.current_app = request.resolver_match.namespace
    blog = Blog.objects.all()
    context = {}
    if blog:
        blog_list = BlogSerializer(blog, many=True)
        #print(type(blog_list.data))
        context = {'blog_list': blog_list.data}
    return render(request, 'index.html', context)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'to_blogId'
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,many=True)
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
        author = MyUser.objects.get(UserInfo=blog.authorId) #反查
        authorInfo = UserInfo.objects.get(userId=author)
        userinfo = UserInfoSerializer(authorInfo)
        BlogNum = Blog.objects.filter(authorId=blog.authorId)
        inter = Interest.objects.filter(Q(toUserId=author), Q(user=user))
        print(userinfo.data)
        resp['blogInfo'] = {'favorNum': len(fav),
                            'isFavou':len(isfav) > 0}
        resp['authorInfo'] = {
                            'BlogNum': len(BlogNum),
                            'UserInfo':userinfo.data,
                            'isIntere': len(inter) >0}
        print(str(resp))
        return JsonResponse(resp)