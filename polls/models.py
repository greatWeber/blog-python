from django.db import models

# Create your models here.

from django.db import models

import uuid

class Member(models.Model):
    name = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    create_time = models.DateField(auto_now_add=True)


class Cate(models.Model):
    cname = models.CharField(max_length=100, default="")
    ename = models.CharField(max_length=100, default="")
    isDel = models.BooleanField(default=False)
    create_time = models.DateField(auto_now_add=True)

class Page(models.Model):
    title = models.CharField(max_length=200, default="")
    author = models.CharField(max_length=100, default="")
    info = models.CharField(max_length=300, default="")
    thumb = models.ImageField(upload_to='thumb')
    content = models.TextField(default="")
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    isDel = models.BooleanField(default=False)
    cateId = models.IntegerField(default=0)


