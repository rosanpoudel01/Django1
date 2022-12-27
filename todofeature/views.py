from django.shortcuts import render
from django import forms
from todofeature.models import Task
from todofeature.forms import TaskForm


# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = "__all__"


# Create your views here.
def todo_list_view(request):
    return render(request, "todo_list.html")


def todo_add_view(request):
    form = TaskForm(request.POST or None)
    return render(
        request, "addtodo.html", {"form": form}
    )  # the dictionary key is passed in form in html file
