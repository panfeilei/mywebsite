from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext,Template,loader
from DjangoUeditor.models import UEditorField
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from testapp.models import  Blog as test_blog
from testapp.models import  Comment, Reply, MyUser
from testapp.models import testmedel
from django.utils.http import urlquote
from apps.users.models import UserInfo

from django.forms.models import model_to_dict
from django.template.loader import render_to_string
import json
from django.core.serializers.json import DjangoJSONEncoder
import time

import operator
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
        return render(request, 'login.html',context={'loginStatus':'True'})
    else:
        return render(request, 'login.html', context={'loginStatus':'False'})
    
def testpost(request):
    #print("get user"+request.GET.get('user', ''))
    t = testmedel()
    print("get user")
    return render(request, 'test.html', {'testfiled':t})

def editor(request):
    return render(request, 'editor.html')

def blog_view(request,id):

    Blog = test_blog.objects.get(blog_id=id)
    return render(request, 'blog.html', {'Blog':Blog})
    
def testView(request):
    return render(request, 'test.html') 
    
@csrf_exempt
def test(request):
    if request.method == 'POST':
        action = request.GET.get('action')
        if action == 'uploadimage':
            img = request.FILES.get('upfile')
            print(request.FILES)
            print(img)
            print(settings.MEDIA_ROOT)
            imgt = open(settings.MEDIA_ROOT+"\\"+img.name, "wb+")
            for l in img.chunks():
                imgt.write(l)
            imgt.close()
            return HttpResponse('{"state": "SUCCESS","url": "http://127.0.0.1:8000/media/%s","title": "dem_title.jpg", "original": "demo_original.jpg"}' %img.name )
    t = Template(r'{"imageActionName":"uploadimage","imageFieldName":"upfile","imageMaxSize":2048000,"imageAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"imageCompressEnable":true,"imageCompressBorder":1600,"imageInsertAlign":"none","imageUrlPrefix":"","imagePathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","scrawlActionName":"uploadscrawl","scrawlFieldName":"upfile","scrawlPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","scrawlMaxSize":2048000,"scrawlUrlPrefix":"","scrawlInsertAlign":"none","snapscreenActionName":"uploadimage","snapscreenPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","snapscreenUrlPrefix":"","snapscreenInsertAlign":"none","catcherLocalDomain":["127.0.0.1","localhost","img.baidu.com"],"catcherActionName":"catchimage","catcherFieldName":"source","catcherPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","catcherUrlPrefix":"","catcherMaxSize":2048000,"catcherAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"videoActionName":"uploadvideo","videoFieldName":"upfile","videoPathFormat":"\/server\/ueditor\/upload\/video\/{yyyy}{mm}{dd}\/{time}{rand:6}","videoUrlPrefix":"","videoMaxSize":102400000,"videoAllowFiles":[".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid"],"fileActionName":"uploadfile","fileFieldName":"upfile","filePathFormat":"\/server\/ueditor\/upload\/file\/{yyyy}{mm}{dd}\/{time}{rand:6}","fileUrlPrefix":"","fileMaxSize":51200000,"fileAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp",".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid",".rar",".zip",".tar",".gz",".7z",".bz2",".cab",".iso",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".txt",".md",".xml"],"imageManagerActionName":"listimage","imageManagerListPath":"\/server\/ueditor\/upload\/image\/","imageManagerListSize":20,"imageManagerUrlPrefix":"","imageManagerInsertAlign":"none","imageManagerAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"fileManagerActionName":"listfile","fileManagerListPath":"\/server\/ueditor\/upload\/file\/","fileManagerUrlPrefix":"","fileManagerListSize":20,"fileManagerAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp",".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid",".rar",".zip",".tar",".gz",".7z",".bz2",".cab",".iso",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".txt",".md",".xml"]}')
    req = RequestContext(request)
    return HttpResponse(t.render(req))
    
@csrf_exempt
def uploadData(request):
    action = request.GET.get('action')
    user = request.user
    if not user.is_authenticated():
        print('no login')
        return HttpResponse('no login')
    if action == "uploadBlog":
        now = time.time()
        title = request.POST.get('title')
        content = request.POST.get('content')
        descript = request.POST.get('descript')
        autor = UserInfo.objects.get(userId=user.userId)
        blog_id = str(hash(str(now) + title)).replace('-', '')
        link = "http://127.0.0.1:8000/blog?title=%s&id=%s" %  (urlquote(title), blog_id)
        b = test_blog(title=title, content=content, link=link, descript=descript, blog_id=blog_id, author=autor.name)
        b.save()
        
    elif action == "uploadComment":
        content = request.POST.get('content')
        to_blogId = request.POST.get('to_blogId')
        #username = request.user.username
        #headlink = request.user.headlink
        userid = request.user.userid
        print('userid is %d' %userid)
        c = Comment(content=content, to_blogId=to_blogId, userid=userid)
        c.save()
    elif action == "uploadReply":
        content = request.POST.get('content')
        to_blogId = request.POST.get('toblogId')
        to_commentId = request.POST.get('toCommentId')
        to_username = request.POST.get('toUsername')
        userid = request.user.userid
        r = Reply(content=content, to_blogId=to_blogId, to_commentId=to_commentId, userid=userid, to_username=to_username)
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
    
def getdata(request):
    action = request.GET.get('action')
    if action == "getComment":
        blog_id = request.GET.get('blogid')
        comment_list = []
        comment = Comment.objects.filter(to_blogId=blog_id).order_by('time')
        reply_all = Reply.objects.filter(to_blogId=blog_id)
        for c in comment:
            comentjson = c.toJSON()
            user = MyUser.objects.get(userid=c.userid)
            print(c.time.strftime('%a, %b %d %H:%M'))
            comentjson['username'] = user.username
            comentjson['headlink'] = user.headlink
            reply_list = []
            reply = reply_all.filter(to_commentId=c.comment_id)
            for r in reply:
                reply_item = r.toJSON()
                user_item = MyUser.objects.get(userid=c.userid)
                reply_item['username'] = user_item.username
                reply_item['headlink'] = user_item.headlink
                reply_list.append(reply_item)
            comentjson['reply_list'] = reply_list
            comment_list.append(comentjson)
        return HttpResponse(json.dumps(comment_list, cls=DjangoJSONEncoder))
    return HttpResponse('None')
    
@login_required
def index(request):
    request.current_app = request.resolver_match.namespace
    t = loader.get_template('index.html')
    blog_list = test_blog.objects.all()
    context = {}
    if blog_list:
        context = {'blog_list': blog_list}
    return render(request, 'index.html', context)