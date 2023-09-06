from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TaskPost

class TaskPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('blog_post',)

admin.site.register(TaskPost, TaskPostAdmin)