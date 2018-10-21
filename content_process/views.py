from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print('执行view代码。。。。')
    return HttpResponse('ok')