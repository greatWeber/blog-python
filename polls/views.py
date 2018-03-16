from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from django.contrib.auth import login, logout, authenticate

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

            data = {'status':0,'info':'登陆失败','url':'/polls/mlogin'}
        return JsonResponse(data)
    else:
        return render(request,'polls/login.html')
