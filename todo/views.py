from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ArticleAPIView (APIView):
    def get(self, request):
        queryset = Article.objects.all()
        return Response({'article': ArticleSerializer(queryset, many=True).data})


    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'article': serializer.data})


    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed1"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesn't exists"})

        serializer = ArticleSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'article': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method DELETE not allowed1"})

        try:
            instance = Article.objects.get(pk=pk)
        except:
            return Response({"error": "Object doesn't exists"})

        instance.delete()

        return Response({'article': "delete article " + str(pk)})
