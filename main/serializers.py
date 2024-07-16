from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed', 'owner')
