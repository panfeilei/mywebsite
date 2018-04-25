from django.conf.urls import url,include
from apps.users import views as user_view
urlpatterns = [
    url(r'^PersonalZone/(?P<userId>\w+)/', user_view.home, name='PersonalZoneUrl'),
    url(r'^apply/', user_view.apply, name='apply'),
]