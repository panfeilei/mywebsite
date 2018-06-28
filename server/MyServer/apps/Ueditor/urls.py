from django.conf.urls import url,include

from .views import get_ueditor_controller
app_name = 'editor'
urlpatterns = [
    url(r'^', get_ueditor_controller),
]