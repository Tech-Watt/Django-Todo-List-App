from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .form import TodoForm 
from .models import Todo
# Create your views here.
def homepage(request):
    return render(request,'todo/home.html')

def create_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(create_todo)
        else:
            return HttpResponse('Invalid Todo Data')

    return render(request,'todo/create_todo.html',{'form':form})


def view_todo(request):
    todos = Todo.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST:
            todo_id = request.POST.get('delete')
            todo = Todo.objects.get(id=todo_id)
            todo.delete()
            return redirect(view_todo)
        
        elif 'edit' in request.POST:
            todo_id =  request.POST.get('edit')
            return redirect(edit_todo,todo_id = todo_id)

    return render(request,'todo/view_todo.html',{'todos':todos})


def edit_todo(request, todo_id):
    todo = get_object_or_404(Todo,id= todo_id)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance =todo)
        if form.is_valid():
            form.save()
            return redirect(view_todo)
    else:
        form = TodoForm(instance=todo)
        
    return render(request,'todo/edit_todo.html',{'form':form})