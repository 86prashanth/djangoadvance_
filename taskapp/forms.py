from django_summernote.widgets import SummernoteWidget
from django import forms
from taskapp.models import TaskPost

class PostForm(forms.ModelForm):
   class Meta:
      model = TaskPost
      fields = ['title', 'category_name', 'blog_post']
      widgets = {'blog_post': SummernoteWidget()}