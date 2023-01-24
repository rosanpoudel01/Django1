from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from todofeature.models import Task
from todofeature.forms import TaskForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# class TodoForm(forms.ModelForm):
#     class Meta:
#         model = Task
#         fields = "__all__"


# Create your views here.
def todo_list_view(request):
    tasks = Task.objects.all().order_by("-id")

    return render(request, "todo_list.html", {"tasks": tasks})


def todo_add_view(request):
    form = TaskForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))
    return render(
        request, "addtodo.html", {"form": form}
    )  # the dictionary key is passed in form in html file


def todo_edit_view(request, taskid):
    task = get_object_or_404(Task, id=taskid)
    # try:
    #     Task.objects.get(id=taskid)
    # except Task.DoesNotExist:
    #     raise Http404()  import HTTp404 first
    form = TaskForm(request.POST or None, request.FILES or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("todofeature:todo_list"))

    return render(request, "addtodo.html", {"form": form})


def todo_delete_view(request):
    taskid = request.POST.get("taskid")
    task = get_object_or_404(Task, id=taskid)
    task.delete()
    return HttpResponseRedirect(reverse("todofeature:todo_list"))


def demo_for_ajax(request):
    data = {"name": "Ram", "address": "Kathmandu"}
    return JsonResponse(data, safe=False)
