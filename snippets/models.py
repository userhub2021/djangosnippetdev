from turtle import Turtle, title
from venv import create
from django.db import models
from django.conf import settings
# Create your models here.

class Snippet(models.Model):
    title = models.CharField('タイトル', max_length=120)
    code = models.TextField('コード', blank=True)
    description = models.TextField("説明", blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='投稿者',on_delete=models.CASCADE)
    created_at =models.DateTimeField('投稿日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title   