from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def home(request):
    form=PostForm()
    return render(request,'htmleditor/home.html',{'form':form})


# email sender
def sendanemail(request):
    if request.method == "POST":
        to = request.POST.get('toemail')
        content = request.POST.get('content')
        send_mail(
            #subject
            "testing",
            #message
            content,
            #from email
            settings.EMAIL_HOST_USER,
            #recipent list
            [to]
        )
        return render(
        request,
        'htmleditor/email.html',
        {
        'title':'send an email'
        }
    )
    else:
        return render(
        request,
        'htmleditor/email.html',
        {
        'title':'send an email'
        }
    )


