from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from todo.models import Task
from todo import serializers
# Create your views here.

class TaskList(APIView):
    

    def get(self,request):
        tasks= Task.objects.order_by('start_time')
        recent_serializer=serializers.TaskSerializer(tasks[0:3],many=True)
        all_serializer=serializers.TaskSerializer(tasks,many=True)

        data_dict = {
            "recent tasks":recent_serializer.data,
            "all tasks":all_serializer.data,
        }

        return Response(data_dict)

    def post(self,request):
        serializer=serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"task saved as":serializer.data})


class Taskk(APIView):

    def get(self,request,id):
        task=Task.objects.get(pk=id)
        serializer = serializers.TaskSerializer(task)

        return Response(serializer.data)

