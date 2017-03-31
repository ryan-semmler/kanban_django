from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET'])
def view_all_tasks(request):
    ''' view all tasks '''
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    # permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    return Response(serializer.data)

@api_view(['GET'])
def view_task_detail(request, detail_id):
    '''view all details for one task'''
    specific_task = Task.objects.get(id=detail_id)
    serializer = TaskSerializer(specific_task, many=False)
    # permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    return Response(serializer.data)

@api_view(['GET'])
def delete_task(request, detail_id):
    '''delete a single task'''
    trash_task = Task.objects.get(id=detail_id)
    if trash_task.delete():
        return "success"
    else:
        return "error"
