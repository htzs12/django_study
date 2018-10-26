from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from django.core.cache.backends.memcached import MemcachedCache


def index(request):
    cache.set('username','haha',100)
    username = cache.get('username')
    print(username)
    return HttpResponse('index')
