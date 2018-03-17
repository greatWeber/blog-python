from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

#from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

from .models import Member ,Cate

def index(request):
	return HttpResponse('hello welcome to Django!')


def mlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        psd = request.POST.get('password','')
        user = Member.objects.filter(name=name, password=psd).get()
        print(user)
        if user:
            request.session['username']=user.name
            data = {'status':1,'info':'登陆成功','url':'/polls/index'}
        else:

            data = {'status':0,'info':'登陆失败','url':'/polls/login'}
        return JsonResponse(data)
    else:
        return render(request,'polls/login.html')


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

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/polls/login')

def check_login(request):
    if request.session['username'] is None:
        return HttpResponseRedirect('/polls/login')

def mindex(request):
    check_login(request)
    content = {'username':request.session['username']}
    return render(request, 'polls/mindex.html', content)
