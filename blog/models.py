from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
@receiver(post_save, sender = Post)
def send_notification(sender, instance, created, **kwargs):
    if created:
        subject = "New blog post created"
        message = 'A new blog post "{}" has been created.'.format(instance.title)
        send_mail(subject, message, 'iamtheks9004@gmail.com',['prashanth.marolix@gmail.com'])