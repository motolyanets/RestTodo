from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "content", "createdAt", "executor")


class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executors
        fields = ("id", "name")
