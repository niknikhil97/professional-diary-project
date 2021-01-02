from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView 
from todo.models import Task
from todo import serializers
# Create your views here.

class TasksList(APIView):
    

    def get(self,request):
        tasks=Task.objects.all()
        serializer=serializers.TaskSerializer(tasks,many=True)
        
        return Response({"all tasks":serializer.data})

    def post(self,request):
        serializer=serializers.TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({"task saved as":serializer.data})