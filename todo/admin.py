from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Article._meta.fields]

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)
# admin.site.register(Executors)
admin.site.register(MyUser)
