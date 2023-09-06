from django.shortcuts import render,redirect
from Todolist.models import Todo

# Create your views here.
def index(request):
    todo = Todo.objects.all()

    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('index')


    return render(request, 'todo/index.html', {'todos': todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('index')
# Create your views here.
