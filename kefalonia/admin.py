from django.contrib import admin

from embed_video.admin import AdminVideoMixin

from .models import Place


class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Place, AdminVideo)
