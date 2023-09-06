from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.forms import PostForm
from datetime import datetime


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("You have created the Post successfully")
        
    else:
        form = PostForm()
        
    return render(request, 'blog/create_post.html',{'form':form})

# convert date time to string
now = datetime.now() 

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	