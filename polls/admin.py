from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Cate, Member, Page

admin.site.register(Member)
admin.site.register(Cate)
admin.site.register(Page)

