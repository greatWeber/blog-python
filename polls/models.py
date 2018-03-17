from django.db import models

# Create your models here.

from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    create_time = models.DateField(auto_now_add=True)


class Cate(models.Model):
    cname = models.CharField(max_length=100, default="")
    ename = models.CharField(max_length=100, default="")
    create_time = models.DateField(auto_now_add=True)
