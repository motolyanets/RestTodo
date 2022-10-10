from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import *


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all().order_by('createdAt')
    serializer_class = ArticleSerializer
    # permission_classes = (IsAuthenticated, )

    def filter_queryset(self, queryset):
        executor_id = self.request.query_params.get('executor')
        if executor_id:
            queryset = queryset.filter(executor__id=executor_id)
        return queryset


class ExecutorViewSet(ListModelMixin, GenericViewSet):
    queryset = MyUser.objects.all().order_by('id')
    serializer_class = ExecutorSerializer
    # permission_classes = (IsAuthenticated,)
