from django.contrib import admin

from apps.blogs.models import MyUser, Blog

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Blog)