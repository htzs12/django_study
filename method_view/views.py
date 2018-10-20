from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,JsonResponse
import json


def index(request):
    print(request.get_host())
    print(request.GET)
    username = request.GET.get('username',default='haha')
    print(username)
    return HttpResponse('success')


def index1(request):
    person = {
        'username':'haoge',
        'age':20
    }
    # person_str = json.dumps(person)
    # response = HttpResponse(person_str,content_type='application/json')
    response = JsonResponse(person,safe=False) # safe=False 非字典类型需要设置
    return response
