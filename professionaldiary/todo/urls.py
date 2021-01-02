from django.urls import path,include
from todo import views

urlpatterns = [
    path('',views.TasksList.as_view())
]