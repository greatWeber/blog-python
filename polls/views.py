from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

#from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

from .models import Member ,Cate, Page

import os

import uuid

import datetime as dt

from django.conf import settings

def index(request):
	return HttpResponse('hello welcome to Django!')

#登陆
def mlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        psd = request.POST.get('password','')
        user = Member.objects.filter(name=name, password=psd).get()
        print(user)
        if user:
            request.session['username']=user.name
            data = {'status':1,'info':'登陆成功','url':'/polls/mindex'}
        else:

            data = {'status':0,'info':'登陆失败','url':'/polls/login'}
        return JsonResponse(data)
    else:
        return render(request,'polls/login.html')

#注册
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        psd = request.POST.get('password','')
        repsd = request.POST.get('repassword','')
        if psd != repsd:
            data = {'status':-1,'info':'确认密码不一致','url':'/polls/register'}
        elif Member.objects.filter(name=name):
            data = {'status':-2,'info':'已存在用户','url':'/polls/register'}
        else:
            user = Member.objects.create(name=name,password=psd)
            user.save();
            if user.id:
                data = {'status':1,'info':'注册成功','url':'/polls/login'}
            else:
                data = {'status':0,'info':'注册失败','url':'/polls/register'}

        return JsonResponse(data)
    else:
        return render(request,'polls/register.html')

#退出登陆
def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/polls/login')

#检查登陆
def check_login(request):
    if request.session['username'] is None:
        return HttpResponseRedirect('/polls/login')
#后台首页
def mindex(request):
    check_login(request)
    content = {'username':request.session['username'],'title':'index'}
    return render(request, 'polls/mindex.html', content)

#分类列表
def cateIndex(request):
    check_login(request)
    list = Cate.objects.filter(isDel=False)
    #print(list)
    content = {'username':request.session['username'],'title':'cate','list':list}
    return render(request,'polls/cateIndex.html',content)

#添加分类
def cateAdd(request):
    check_login(request)
    if request.method == 'GET':
         content = {'username':request.session['username'],'title':'cate'}
         return render(request,'polls/cateAdd.html',content)
    else:
         cname = request.POST.get('cname','')
         ename = request.POST.get('ename','')
         cate = Cate.objects.create(cname=cname, ename=ename)
         cate.save()
         if cate.id:
             data = {'status':1,'info':'分类添加成功','url':'/polls/cateIndex'}
         else:
             data = {'status':0,'info':'分类添加失败','url':'/polls/cateAdd'}
         return JsonResponse(data)

#编辑分类
def cateEdit(request):
    check_login(request)
    if request.method == 'GET':
        id = request.GET.get('id',0)
        cate = Cate.objects.filter(id=id).get()
        content = {'username':request.session['username'],'title':'cate','cate':cate}
        return render(request,'polls/cateEdit.html',content)
    else:
         cname = request.POST.get('cname','')
         ename = request.POST.get('ename','')
         id = request.POST.get('id',0)
         cate = Cate.objects.filter(id=id).get()
         cate.cname = cname
         cate.ename = ename
         cate.save()
         if cate.id:
             data = {'status':1,'info':'分类编辑成功','url':'/polls/cateIndex'}
         else:
             data = {'status':0,'info':'分类编辑失败','url':'/polls/cateEdit'}
         return JsonResponse(data)

#删除分类
def cateDel(request):
    check_login(request)
    ids =  request.POST.get('id','')
    Ids = ids.split(',')
    for id in Ids:
        cate = Cate.objects.get(id=id)
        cate.isDel = True
        cate.save()
    isDel = True
    for id in Ids:
        if Cate.objects.get(id=id).isDel == False:
            isDel = False
    if isDel:
        data = {'status':1,'info':'删除成功'}
    else:
        data = {'status':0,'info':'删除失败'}
    return JsonResponse(data)

#文章列表
def pageIndex(request):
    check_login(request)
    list = Page.objects.filter(isDel=False)
    #print(list)
    content = {'username':request.session['username'],'title':'page','list':list}
    return render(request,'polls/pageIndex.html',content)

#添加文章
def pageAdd(request):
    check_login(request)
    if request.method == 'GET':
         content = {'username':request.session['username'],'title':'page'}
         return render(request,'polls/pageAdd.html',content)
    else:
         title = request.POST.get('title','')
         author = request.POST.get('author','')
         author = request.session['username'] if author == '' else author
         thumb = request.FILES.get('thumb','')
         info= request.POST.get('info','')
         content= request.POST.get('content','')
         page = Page.objects.create(title=title,author=author, thumb=thumb, info=info, content=content)
         page.save()
         if page.id:
             data = {'status':1,'info':'文章添加成功','url':'/polls/pageIndex'}
         else:
             data = {'status':0,'info':'文章添加失败','url':'/polls/pageAdd'}
         return JsonResponse(data)

#编辑文章
def pageEdit(request):
    check_login(request)
    if request.method == 'GET':
        id = request.GET.get('id',0)
        page = Page.objects.filter(id=id).get()
        content = {'username':request.session['username'],'title':'page','page':page}
        return render(request,'polls/pageEdit.html',content)
    else:
         id = request.POST.get('id',0)
         title = request.POST.get('title','')
         author = request.POST.get('author',request.session['username'])
         thumb = request.FILES.get('thumb','')
         info= request.POST.get('info','')
         content= request.POST.get('content','')
         page = Page.objects.filter(id=id).get()
         page.title = title
         page.author = author
         if thumb != '':
             page.thumb = thumb
         page.info = info
         page.content = content
         page.save()
         if page.id:
             data = {'status':1,'info':'文章编辑成功','url':'/polls/pageIndex'}
         else:
             data = {'status':0,'info':'文章编辑失败','url':'/polls/pageEdit'}
         return JsonResponse(data)
#删除文章
def pageDel(request):
    check_login(request)
    ids =  request.POST.get('id','')
    Ids = ids.split(',')
    for id in Ids:
        page = Page.objects.get(id=id)
        page.isDel = True
        page.save()
    isDel = True
    for id in Ids:
        if Page.objects.get(id=id).isDel == False:
            isDel = False
    if isDel:
        data = {'status':1,'info':'删除成功'}
    else:
        data = {'status':0,'info':'删除失败'}
    return JsonResponse(data)

def upload(request):
    dir_name = 'images'
    result = {'success':False,'msg':'上传出错'}
    files = request.FILES.get('upload_file',None)
    if files:
        result = image_upload(files, dir_name)
    return JsonResponse(result)

def image_upload(files, dir_name):
    allow_suffix = ['jpg','jpeg','png']
    file_suffix = files.name.split('.')[-1]
    if file_suffix not in allow_suffix:
        return {'success':False,'msg':'图片格式不对'}
    file_path = mkdir_upload_path(dir_name)
    path = os.path.join(settings.MEDIA_ROOT,file_path)
    if not os.path.exists(path):
        os.makedirs(path)
    file_name = str(uuid.uuid1())+'.'+file_suffix
    path_file = os.path.join(path, file_name)
    file_url = settings.MEDIA_URL+file_path+file_name
    open(path_file,'wb').write(files.file.read())
    return {'success':True,'msg':'图片上传成功','file_path':file_url}

def mkdir_upload_path(dir_name):
    today = dt.datetime.today()
    dir_name = dir_name+'/%d/%d/' %(today.year, today.month)
    return dir_name
