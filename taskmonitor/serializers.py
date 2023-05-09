from rest_framework import serializers
from .models import User, TaskMonitor, Task

class TaskMonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMonitor
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'