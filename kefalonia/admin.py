from django.contrib import admin
from django.contrib.auth.models import User

from embed_video.admin import AdminVideoMixin

from .models import Youtube
from .models import Place


# Register your models here.
admin.site.register(Place)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Youtube, MyModelAdmin)