from django.urls import path
from todofeature.views import (
    todo_list_view,
    todo_add_view,
    todo_edit_view,
    todo_delete_view,
    demo_for_ajax,
)

app_name = "todofeature"
urlpatterns = [
    path("", todo_list_view, name="todo_list"),
    path("todo-add/", todo_add_view, name="todo_add"),
    path("todo-edit/<int:taskid>/", todo_edit_view, name="todo_edit"),
    path("todo-delete/", todo_delete_view, name="todo_delete"),
    path("demo-for-ajax", demo_for_ajax, name="demo_for_ajax"),
]
