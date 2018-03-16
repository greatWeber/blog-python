from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

def index(request):
	return HttpResponse('hello welcome to Django!')


def mlogin(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        psd = request.POST.get('password','')
        user = authenticate(username=name,password=psd)
        if user is not None:
            login(request, user)
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
        elif User.objects.filter(username=name):
            data = {'status':-2,'info':'已存在用户','url':'/polls/register'}
        else:
            user = User.objects.create_user(username=name,password=psd,email='')
            user.save();
            if user.id:
                data = {'status':1,'info':'注册成功','url':'/polls/login'}
            else:
                data = {'status':0,'info':'注册失败','url':'/polls/register'}

        return JsonResponse(data)
    else:
        return render(request,'polls/register.html')
