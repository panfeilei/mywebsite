from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.template import RequestContext,Template
from DjangoUeditor.models import UEditorField
# Create your views here.
class dd():
    f=4


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
    return HttpResponse('logindddtest')

def editor(request):
    return render(request, 'editor.html')

def test(request):
    print("tttt")
    return HttpResponse(r'{"imageActionName":"uploadimage","imageFieldName":"upfile","imageMaxSize":2048000,"imageAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"imageCompressEnable":true,"imageCompressBorder":1600,"imageInsertAlign":"none","imageUrlPrefix":"","imagePathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","scrawlActionName":"uploadscrawl","scrawlFieldName":"upfile","scrawlPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","scrawlMaxSize":2048000,"scrawlUrlPrefix":"","scrawlInsertAlign":"none","snapscreenActionName":"uploadimage","snapscreenPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","snapscreenUrlPrefix":"","snapscreenInsertAlign":"none","catcherLocalDomain":["127.0.0.1","localhost","img.baidu.com"],"catcherActionName":"catchimage","catcherFieldName":"source","catcherPathFormat":"\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}","catcherUrlPrefix":"","catcherMaxSize":2048000,"catcherAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"videoActionName":"uploadvideo","videoFieldName":"upfile","videoPathFormat":"\/server\/ueditor\/upload\/video\/{yyyy}{mm}{dd}\/{time}{rand:6}","videoUrlPrefix":"","videoMaxSize":102400000,"videoAllowFiles":[".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid"],"fileActionName":"uploadfile","fileFieldName":"upfile","filePathFormat":"\/server\/ueditor\/upload\/file\/{yyyy}{mm}{dd}\/{time}{rand:6}","fileUrlPrefix":"","fileMaxSize":51200000,"fileAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp",".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid",".rar",".zip",".tar",".gz",".7z",".bz2",".cab",".iso",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".txt",".md",".xml"],"imageManagerActionName":"listimage","imageManagerListPath":"\/server\/ueditor\/upload\/image\/","imageManagerListSize":20,"imageManagerUrlPrefix":"","imageManagerInsertAlign":"none","imageManagerAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp"],"fileManagerActionName":"listfile","fileManagerListPath":"\/server\/ueditor\/upload\/file\/","fileManagerUrlPrefix":"","fileManagerListSize":20,"fileManagerAllowFiles":[".png",".jpg",".jpeg",".gif",".bmp",".flv",".swf",".mkv",".avi",".rm",".rmvb",".mpeg",".mpg",".ogg",".ogv",".mov",".wmv",".mp4",".webm",".mp3",".wav",".mid",".rar",".zip",".tar",".gz",".7z",".bz2",".cab",".iso",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".pdf",".txt",".md",".xml"]}')

@login_required
def index(request):
    #t=Template('index.html')
    c = RequestContext(request, {
        'foo': 'bar',
    })
    #return HttpResponse(t.render(c))
    return render(request, 'index.html')