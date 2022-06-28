from django.db import models


class Article(models.Model):
    content = models.TextField(blank=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    executor = models.ForeignKey('Executors', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.content


class Executors(models.Model):
    name = models.CharField(max_length=40, db_index=True)

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'

    def __str__(self):
        return self.name
