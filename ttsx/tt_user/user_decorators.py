# coding=utf-8

from django.shortcuts import redirect


def user_login(func):
    def fun1(request, *args, **kwargs):
        # 判断用户是否登陆
        if request.session. has_key('uid'):
            # 如果登陆则继续执行试图
            return func(request, *args, **kwargs)
        else:
            # 如果没登陆，跳转到登陆页
            return redirect('/user/login/')
    return fun1