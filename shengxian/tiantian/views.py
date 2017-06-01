# coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from models import *
from hashlib import sha1

# Create your views here.
def index(request):
    return render(request,'tiantian/index.html')

# 注册页
def register(request):
    return render(request,'tiantian/register.html')

# 处理注册
def register_handle(request):
    # 获取
    # 返回数据格式：?user_name=123456&pwd=123456789&cpwd=123456789&email=123456789%40qq.com&allow=on
    user = request.POST
    uname = user['user_name']
    upwd = user['pwd']
    upwd2 = user['cpwd']
    uemail = user['email']

    # 判断密码
    if upwd != upwd2:
        return redirect('/user/register/')
    #　密码加密
    s1 = sha1()
    s1.update(upwd)
    upwd3 = s1.hexdigest()


    # 判断是否存在，存在进行登陆
    # test = UserInfo.objects.filter(uname=uname)
    # print(test)
    # if test:
    #     return HttpResponse("该用户已存在！")

    # 不存在进程注册
    user = UserInfo.objects.create(uname=uname, upwd=upwd3, uemail=uemail)
    user.save()
    return redirect('/user/login/')
    #return HttpResponse("您已注册成功！可以进行登陆了")


# 用户不存在的情况下
def register_exist(request):
    uname = request.GET.get('uname')
    #count = UserInfo.objects.filter(uname = 'a').count()
    count = UserInfo.objects.filter(uname=uname).count()
    #print count
    #return HttpResponse('ok')
    return JsonResponse({'count':count})

def login(request):
    uname = request.COOKIES.get('uname','')
    context = {'title':'用户登陆','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'tiantian/login.html',context)





# 同桌
# def login(request):
#     # 获取注册页发来的POST提交
#     dict = request.POST
#     name = dict.get('user_name')
#     pwd = dict.get('pwd')
#     email = dict.get('email')
#
#     valid = UserInfo.objects.filter(uname=name,upwd=pwd,uemail=email)
#
#     # 判断在数据库是否存在,如果存在则返回注册页,并提示
#     if valid:
#         return redirect("/register",{'valid':'没有该用户'})
#     # 创建数据
#     user = UserInfo.objects.create(uname=name,upwd=pwd,uemail=email)
#     user.save()
#     context = {
#         'name' : name
#     }
#     return render(request, 'df_users/login.html',context)
