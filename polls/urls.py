# urls.py

from django.conf.urls import url

from django.conf.urls.static import static

from django.conf import settings


from . import views

urlpatterns = [
	url(r'/',views.index,name='index'),
	url(r'login',views.mlogin,name='login'),
	url(r'register',views.register,name='register'),
	url(r'mindex',views.mindex,name='mindex'),
	url(r'logout',views.logout,name='logout'),
	url(r'cateIndex',views.cateIndex,name='cateIndex'),
	url(r'cateAdd',views.cateAdd,name='cateAdd'),
	url(r'cateEdit',views.cateEdit,name='cateEdit'),
	url(r'cateDel',views.cateDel,name='cateDel'),
	url(r'pageIndex',views.pageIndex,name='pageIndex'),
	url(r'pageAdds',views.pageAdd,name='pageAdd'),
	url(r'pageEdit',views.pageEdit,name='pageEdit'),
	url(r'upload',views.upload,name='upload'),
]
