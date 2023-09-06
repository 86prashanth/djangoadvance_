from django.db import models
from django.utils import timezone
 
class TaskPost(models.Model):
    category_name = models.CharField(max_length=250, default='basic')
    title = models.CharField(max_length=100)
    blog_post = models.TextField()
    is_active = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title