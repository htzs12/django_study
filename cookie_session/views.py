from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware


def index(request):
    # 操作cookie
    response = HttpResponse('index')
    # expires = datetime(year=2018,month=10,day=21,hour=23,minute=0,second=0)
    # expires = make_aware(expires)
    # response.set_cookie('username','haoge',expires=expires)
    response.set_cookie('username','haoge',max_age=180)
    return response


def my_list(request):
    # 获取cookies
    cookies = request.COOKIES
    username = cookies.get('username')
    return HttpResponse(username)


def del_cookie(request):
    # 删除cookies
    response = HttpResponse('delete')
    response.delete_cookie('username')
    return response


def session_view(request):
    # request.session['username'] = 'haoge'
    # username = request.session.get('username') # 查找
    # username = request.session.pop('username') # 删除
    request.session.flush() # 清除数据库中的session表内容
    # print(username) # haoge
    return HttpResponse('session view')
