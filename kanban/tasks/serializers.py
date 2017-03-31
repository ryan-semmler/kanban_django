from rest_framework import serializers
from .models import Task, STATUS_CHOICE, PRIORITY_CHOICE


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'status', 'priority')
