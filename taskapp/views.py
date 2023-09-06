from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from taskapp.models import TaskPost

def note_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('new form is added')
    else:
        form = PostForm()
        context = {
                'form':form
                }
            
    return render(request, 'task/home.html', context)

def task_list(request):
    post_list = TaskPost.objects.all()
    return render(request, 'task/task_list.html', {'posts': post_list})

def task_view(request,post_id):
    post_view = TaskPost.objects.filter(id=post_id)
    return render(request, 'task/task_view.html', {'post': post_view}) 