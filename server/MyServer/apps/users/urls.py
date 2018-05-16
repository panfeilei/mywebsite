from django.conf.urls import url,include
from apps.users import views as user_view
app_name = 'polls'
urlpatterns = [
    url(r'^PersonalZone/', user_view.home, name='PersonalZoneUrl'),
    url(r'^apply/', user_view.apply, name='apply'),
    url(r'^getMessage', user_view.getMessage),
    url(r'^getmessageinfo', user_view.getMessageInfo, name='getmessageinfo'),
]