# coding=utf-8
import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from hashlib import sha1

from models import UserInfo
from user_decorators import user_login


def register(request):
    return render(request, 'tt_user/register.html', {'title': '注册', 'top':'0'})


def register_handle(request):
    dict = request.POST
    uname = dict.get('user_name')
    upwd = dict.get('pwd')
    ucpwd = dict.get('cpwd')
    email = dict.get('email')

    if upwd != ucpwd:
        return redirect('/user/register/')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    user = UserInfo()
    user.uname = uname
    user.upwd = upwd_sha1
    user.uemail = email
    user.save()

    return redirect('/user/login/')


def register_username(request):
    uname = request.GET.get('uname')
    user = UserInfo.objects.filter(uname=uname).count()
    context = {'username': user}
    return JsonResponse(context)


def login(request):
    uname = request.GET.get('uname')
    context = {'title': '登陆', 'uname': 'uname', 'top': '0'}
    return render(request, 'tt_user/login.html', context)


def login_handle(request):
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    uname_jz = post.get('name_jz', '0')

    s1 = sha1()
    s1.update(upwd)
    upwd_sha1 = s1.hexdigest()

    context = {'title': '登录', 'uname': uname, 'upwd': upwd, 'top': '0'}
    # 根据用户名查询数据，如果未查到返回[]，如果查到则返回[UserInfo]
    users = UserInfo.objects.filter(uname=uname)
    if len(users) == 0:
        # 用户名错误
        context['name_error'] = '1'
        return render(request, 'tt_user/login.html', context)
    else:
        if users[0].upwd == upwd_sha1:  # 登录成功
            # 记录当前登录的用户
            request.session['uid'] = users[0].id
            request.session['uname'] = uname
            # 重定向，即从哪儿来，回哪儿去
            path = request.session.get('url_path', '/')
            response = redirect(path)

            # 记住用户名
            if uname_jz == '1':
                response.set_cookie('uname', uname, expires=datetime.datetime.now() + datetime.timedelta(days=7))
            else:
                response.set_cookie('uname', '', max_age=-1)
            return response
        else:
            # 密码错误
            context['pwd_error'] = '1'
            print '密码错误'
            return render(request, 'tt_user/login.html', context)



def logout(request):
    request.session.flush()
    return redirect('/user/login/')


def islogin(request):
    result = 0
    if request.session. has_key('uid'):
        result = 1
        return JsonResponse({'islogin': result})


def index(request):
    return render(request, 'tt_user/index.html', {'title': '首页'})


@user_login
def center(request):
    return render(request, 'tt_user/order.html', {'title': '用户中心', 'top':'1'})


@user_login
def order(request):
    context = {'title': '用户订单'}
    return render(request, 'tt_user/order.html', context)


@user_login
def site(request):
    user = UserInfo.objects.get(pk=request.session['uid'])
    if request.method == 'POST':
        post = request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('udddress')
        user.uphone = post.get('uphone')
        user.save()

    context = {'title': '收货地址', 'user':user}
    return render(request, 'tt_user/site.html', context)


def cart(request):
    return render(request, 'tt_user/cart.html')



# Create your views here.
