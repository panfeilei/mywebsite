from datetime import datetime
import random
import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from . import settings as USettings

@csrf_exempt
def get_settings(request):
    return JsonResponse(USettings.UPLOADSETTING)

def get_path_format_vars():
    now = datetime.now()
    return {
        'year': now.strftime('%Y'),
        'month': now.strftime('%m'),
        'day': now.strftime('%d'),
        'hour':now.strftime('%H'),
        "rnd": random.randrange(100, 999),
    }

def get_output_file(path_format, var):
    PathForamt = USettings.UPLOADSETTING.get(path_format) % var
    OutPutFullPath = os.path.join(settings.MEDIA_ROOT, PathForamt)
    OutPath ,OutFileName = os.path.split(OutPutFullPath)
    if not os.path.exists(OutPath):
        os.makedirs(OutPath)
    return OutPutFullPath, OutFileName,PathForamt

@csrf_exempt
def UploadFile(request):
    state = "SUCCESS"
    if not request.method == 'POST':
        return HttpResponse('{"status":"error"}')
    action = request.GET.get('action')

    upload_filed_name = {
        "uploadfile": "fileFieldName",
        'uploadimage': 'imageFieldName',
        'uploadvideo': 'videoFieldName',
    }
    UploadFieldName = USettings.UPLOADSETTING.get(upload_filed_name[action], 'upfile')
    uploadFile = request.FILES.get(UploadFieldName, None)
    path_format_var = get_path_format_vars()
    _,extname = os.path.splitext(uploadFile.name)
    print(extname)
    path_format_var.update({
        'filename': uploadFile.name,
        'extname': extname
    })
    upload_filed_format = {
        "uploadfile": "filePathFormat",
        "uploadimage": "imagePathFormat",
        "uploadvideo" : "videoPathFormat",
    }
    FileFullPath, OriginFileName, PathForamt = get_output_file(upload_filed_format[action], path_format_var)
    f = open(FileFullPath, "wb+")
    for l in uploadFile.chunks():
        f.write(l)
    f.close()
    return_info = {
        'url':  PathForamt,
        'original':OriginFileName,
        'state': state,
        'title': OriginFileName,
    }
    return JsonResponse(return_info)

@csrf_exempt
def get_ueditor_controller(request):
    action = request.GET.get('action','')
    responseAction = {
        'config' : get_settings,
        'uploadimage' : UploadFile,
        'uploadvideo' :UploadFile,

    }
    return responseAction[action](request)