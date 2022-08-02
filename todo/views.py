from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ArticleAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = Article.objects.all()
        return queryset.order_by('createdAt')



class ArticleAPIUpdate(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ExecutorAPIList(generics.ListCreateAPIView):
    queryset = Executors.objects.all()
    serializer_class = ExecutorSerializer


class ExecutorsTasksAPIList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        executor_id = self.kwargs['pk']
        return Article.objects.filter(executor__id=executor_id)

