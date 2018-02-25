from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext,Template,loader
from DjangoUeditor.models import UEditorField
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from testapp.models import  Blog as test_blog
from testapp.models import  Comment
from testapp.models import testmedel
from django.utils.http import urlquote
from django.template.loader import render_to_string
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

def blog_view(request):
    title = request.GET.get("title")
    blog_id = request.GET.get("id")
    print(title)
    Blog = test_blog.objects.get(title=title, blog_id=blog_id)
    return render(request, 'blog.html', {'Blog':Blog})
    
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
    if action == "uploadBlog":
        now = time.time()
        title = request.POST.get('title')
        content = request.POST.get('content')
        descript = request.POST.get('descript')
        blog_id = str(hash(str(now) + title))
        link = "http://127.0.0.1:8000/blog?title=%s&id=%s" %  (urlquote(title), blog_id)
        b = test_blog(title=title, content=content, link=link, descript=descript, blog_id = blog_id)
        b.save()
        return HttpResponse('ok')
    elif action == "uploadComment":
        content = request.POST.get('content')
        to_blogId = request.POST.get('to_blogId')
        #username = request.user.username
        #headlink = request.user.headlink
        userid = request.user.id
        print('userid is %d' %userid)
        c = Comment(content=content, to_blogId=to_blogId, userid=userid)
        c.save()
        return HttpResponse('ok')

def getdata(request):
    return HttpResponse('None')
    
@login_required
def index(request):
    t = loader.get_template('index.html')
    blog_list = test_blog.objects.all()
    context = {}
    if blog_list:
        context = {'blog_list': blog_list}
    return render(request, 'index.html', context)