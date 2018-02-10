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
from DjangoUeditor import views as editor_view

urlpatterns = [
    url(r"^$", test_view.index),
    url(r"^index", test_view.index),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', test_view.mylogin,name='login'),
    url(r'^test1/', test_view.testpost),
    #url(r'^tinymce/', include('tinymce.urls')),
    url(r'^editor/',test_view.editor),
    url(r'^constrol/', editor_view.get_ueditor_controller),
    url(r'^test/',test_view.test),
]
