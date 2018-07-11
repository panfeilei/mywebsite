"""MyServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from DjangoUeditor import views as editor_view
from apps.blogs import views as test_view
from apps.operation import views as operate_view
from apps.users.views import BlogMsgViewSet

router = DefaultRouter()
router.register(r'blogs', test_view.BlogViewSet, base_name='title')
router.register(r'getcomment', test_view.CommentViewSet, base_name='getcomment1')
router.register(r'getreply', test_view.ReplyViewSet)
router.register(r'favourite', operate_view.FavouViewSet)
router.register(r'interest', operate_view.InterViewSet, base_name='interest')
router.register(r'testview', test_view.testViewSet)


urlpatterns = [
    url(r"^$", test_view.defaulInex),
    url(r'^', include(router.urls)),
    url(r"^index/(?P<module>(\w)*)", test_view.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', test_view.mylogin, name='login'),
    url(r'^logout/', test_view.mylogout, name='logout'),
    url(r'^uploadData/', test_view.uploadData),
    url(r'^editor/',test_view.editor, name='edi'),
    url(r'^test1/', test_view.test1),
    url(r'^blogInfo/(?P<blogId>(\w)*)/', test_view.BlogInfo.as_view()),
    url(r'^blog/(\w+)/', test_view.blog_view, name="blogUrl"),
    url(r'^upload-icon/', test_view.uploadIcon, name='uploadIconUrl'),
    url(r'^ueditor/', include('apps.Ueditor.urls', namespace='editor')),
    url(r'^users/', include('apps.users.urls', namespace='userapp')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #url(r'^media/(?P<path>.*)/$', serve, {"document_root": settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)