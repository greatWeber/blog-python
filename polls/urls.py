# urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'/',views.index,name='index'),
	url(r'login',views.mlogin,name='login'),
	url(r'register',views.register,name='register'),
]
