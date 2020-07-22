from rest_framework import serializers
from .models import Dev, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["id"]

class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dev
        projects = ProjectSerializer(many=True)
        fields = ["id", "name", "email", "joined", "projects"]
        read_only_fields = ["id", "joined", "projects"]