
UPLOADSETTING = {
    "imageActionName": "uploadimage",
    "imageFieldName": "upfile",
    "imageMaxSize": 2048000,
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],
    "imageCompressEnable": True,
    "imageCompressBorder": 1600,
    "imageInsertAlign": "none",
    "imageUrlPrefix": "",
    "imagePathFormat": r"image/%(year)s%(month)s%(day)s%(rnd)s%(extname)s",

    #涂鸦图片上传
    "scrawlActionName": "uploadscrawl",
    "scrawlFieldName": "upfile",
    "scrawlPathFormat": "\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}",
    "scrawlMaxSize": 2048000,
    "scrawlUrlPrefix": "",
    "scrawlInsertAlign": "none",

    # 截图工具上传
    "snapscreenActionName": "uploadimage",
    "snapscreenPathFormat": "\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}",
    "snapscreenUrlPrefix": "",
    "snapscreenInsertAlign": "none",

    # 抓取远程图片配置
    "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
	"catcherActionName": "catchimage",
	"catcherFieldName": "source",
	"catcherPathFormat": "\/server\/ueditor\/upload\/image\/{yyyy}{mm}{dd}\/{time}{rand:6}",
	"catcherUrlPrefix": "",
	"catcherMaxSize": 2048000,
	"catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],

    #上传视频配置
    "videoActionName": "uploadvideo",
	"videoFieldName": "upfile",
	"videoPathFormat": r"vedio/%(year)s%(month)s%(day)s%(rnd)s%(extname)s",
	"videoUrlPrefix": "",
	"videoMaxSize": 102400000,
	"videoAllowFiles": [".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg", ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"],

    #上传文件配置
    "fileActionName": "uploadfile",
	"fileFieldName": "upfile",
	"filePathFormat": "\/server\/ueditor\/upload\/file\/{yyyy}{mm}{dd}\/{time}{rand:6}",
	"fileUrlPrefix": "",
	"fileMaxSize": 51200000,
	"fileAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg", ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid", ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"],

    #列出指定目录下的图片
    "imageManagerActionName": "listimage",
    "imageManagerListPath": "\/server\/ueditor\/upload\/image\/",
    "imageManagerListSize": 20,
    "imageManagerUrlPrefix": "",
    "imageManagerInsertAlign": "none",
    "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"],

    #列出指定目录下的文件
    "fileManagerActionName": "listfile",
    "fileManagerListPath": "\/server\/ueditor\/upload\/file\/",
    "fileManagerUrlPrefix": "",
    "fileManagerListSize": 20,
    "fileManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb",
                              ".mpeg", ".mpg", ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
                              ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso", ".doc", ".docx", ".xls",
                              ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"]

}