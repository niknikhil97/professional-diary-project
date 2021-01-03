from django.urls import path,include
from todo import views

urlpatterns = [
    path('tasks/',views.TaskList.as_view()),
    path('task/<int:id>/',views.Taskk.as_view()),
]