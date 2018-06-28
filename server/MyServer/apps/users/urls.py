from django.conf.urls import url,include
from apps.users import views as user_view
from rest_framework.routers import DefaultRouter

from .views import BlogMsgViewSet,AllMsgViewSet, UserMsgViewSet
app_name = 'polls'

router = DefaultRouter()
router.register(r'getmsginfo', AllMsgViewSet, base_name='allmsg')
router.register(r'usermessage', UserMsgViewSet, base_name='usermsg')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^PersonalZone/(?P<userId>(\d)*)', user_view.home, name='PersonalZoneUrl'),
    url(r'^apply/', user_view.apply, name='apply'),
    url(r'^getMessage', user_view.getMessage),
    url(r'^getmessageinfo/', user_view.getMessageInfo, name='getmessageinfo'),

]