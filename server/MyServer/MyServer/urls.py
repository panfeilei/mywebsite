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
from django.conf.urls import url,include
from django.contrib import admin
from testapp import views as test_view
from django.contrib.staticfiles import views as sview
from DjangoUeditor import views as editor_view
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    url(r"^$", test_view.index),
    url(r"^index", test_view.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', test_view.mylogin, name='login'),
    url(r'^logout/', test_view.mylogout, name='logout'),
    url(r'^test1/', test_view.testpost),
    url(r'^uploadData/', test_view.uploadData),
    url(r'^getdata/', test_view.getdata),
    url(r'^editor/',test_view.editor, name='edi'),
    url(r'^constrol/', editor_view.get_ueditor_controller),
    url(r'^test/',test_view.test),
    url(r'^blog/(\w+)/', test_view.blog_view, name="blogUrl"),
    url(r'^users/', include('apps.users.urls', namespace='users', app_name='userapp')),
    #url(r'^media/(?P<path>.*)/$', serve, {"document_root": settings.MEDIA_ROOT}),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)