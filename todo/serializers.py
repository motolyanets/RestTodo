from rest_framework import serializers
from .models import *


class ArticleSerializer(serializers.Serializer):
    content = serializers.CharField()
    createdAt = serializers.DateTimeField(read_only=True)
    executor_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        instance.executor_id = validated_data.get('executor_id', instance.executor_id)
        instance.save()
        return instance

