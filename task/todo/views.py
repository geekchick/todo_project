from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ToDoForm
from .models import ToDo

# Create your views here.
def index(request):
    todos = ToDo.objects.all()
    form = ToDoForm()
    

    if request.method == "POST":
        form = ToDoForm(request.POST) 
        if form.is_valid():
            form.save()
        return redirect("/")
   
    context = {'todos':todos, 'form':form}
    return render(request, 'todo/index.html', context)

def edit(request, pk):
    get_todo_item = ToDo.objects.get(id=pk)
    edit_form = ToDoForm(instance=get_todo_item)

    if request.method == "POST":
        edit_form = ToDoForm(request.POST, instance=get_todo_item)
        if edit_form.is_valid():
            edit_form.save()
            return redirect("/")

    context = {'form':edit_form}
    return render(request, "todo/item.html", context)

def delete(request, pk):
    get_todo_item = ToDo.objects.get(id=pk)

    if request.method == "POST":
        get_todo_item.delete()
        return redirect("/")

    context = {'item': get_todo_item}

    return render(request, "todo/delete.html", context)

