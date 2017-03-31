from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .forms import TaskForm

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


def new_task(request):
    '''loads form to create a new task'''
    new_task = TaskForm()
    return render(request, "template/tasks/create.html", {"task_form": new_task })


@api_view(['POST'])
def add_task_to_DB(request, form_info):
    ''' sends form info to db as a new task'''
    new_task = Task(form_info)
    data = JSONparser().parse(new_task)
    serializer = TaskSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)
